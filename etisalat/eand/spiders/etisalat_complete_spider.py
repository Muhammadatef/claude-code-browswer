"""
Etisalat UAE Complete Spider - IMMEDIATE CSV WRITING VERSION
=============================================================

Key Features:
- Writes each row to CSV IMMEDIATELY after scraping (no batching)
- Two-stage extraction: Outer Card + Side Panel
- Dedicated output folders: etisalat_output/ and etisalat_debug/
- Direct CSV file handling (bypasses Scrapy's feed exporter for instant writes)

Author: Mohamed Atef Fahmi
Date: 2025-11-21
Version: 4.0 (Immediate CSV Writing)
"""

import scrapy
import json
import re
import time
import subprocess
import csv
from datetime import datetime
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from eand.items_selenium import EtisalatPlanItem


class EtisalatCompleteSpider(scrapy.Spider):
    """Complete spider with immediate CSV writing"""

    name = "etisalat_complete"
    allowed_domains = ["etisalat.ae"]

    # Generate output path at class level
    OUTPUT_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

    custom_settings = {
        # Disable Scrapy's built-in feed exporter since we're writing directly to CSV
        'FEEDS': {},
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 5,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create dedicated output folders
        self.output_dir = Path("etisalat_output")
        self.output_dir.mkdir(exist_ok=True)

        self.debug_dir = Path("etisalat_debug")
        self.debug_dir.mkdir(exist_ok=True)

        # Initialize CSV file immediately
        self.csv_filename = self.output_dir / f"etisalat_complete_{self.OUTPUT_TIMESTAMP}.csv"
        self.csv_file = None
        self.csv_writer = None
        self.csv_headers = [
            'Link', 'Name', 'Price_Actual',
            'Main_Group', 'Group', 'Navigational_Aid',
            'Speed', 'Local_Data', 'Roaming_Data',
            'Minutes', 'Minutes_Category',
            'Variable', 'Variable_value',
            'Entertainment_Packs_Data', 'Entertainment_Pack', 'UAE_WiFi_Hours',
            'Additional_Benefits',
            'Promotion', 'Commitment',
            'GTIN_Code', 'UAE_GTIN', 'EAN_Code',
            'scrape_ts', 'insert_ts', 'frequency', 'domain'
        ]
        self.init_csv()

        # Fix ChromeDriver version mismatch before starting
        self.fix_chromedriver_cache()

        # Load discovered URLs from JSON (if available)
        self.discovered_urls = self.load_discovered_urls()

        self.plans_extracted = 0
        self.pages_scraped = 0
        self.validation_warnings = 0

        # Track processed plans to avoid duplicates
        self.processed_plans = set()

        # Statistics for plan counting
        self.plans_by_category = {
            'prepaid': 0,
            'visitor': 0,
            'postpaid': 0
        }

        # Build start URLs
        self.start_urls = self.build_start_urls()

        self.logger.info("\n" + "="*100)
        self.logger.info("  🚀 ETISALAT UAE COMPLETE SPIDER - IMMEDIATE CSV WRITING")
        self.logger.info("="*100)
        self.logger.info(f"  Total URLs to scrape: {len(self.start_urls)}")
        self.logger.info(f"  Output folder: {self.output_dir.absolute()}")
        self.logger.info(f"  CSV File: {self.csv_filename}")
        self.logger.info(f"  ✅ CSV will be written IMMEDIATELY after each plan is scraped")
        self.logger.info("="*100 + "\n")

    def init_csv(self):
        """Initialize CSV file with headers immediately"""
        try:
            self.csv_file = open(self.csv_filename, 'w', newline='', encoding='utf-8-sig')
            self.csv_writer = csv.DictWriter(self.csv_file, fieldnames=self.csv_headers)
            self.csv_writer.writeheader()
            self.csv_file.flush()  # Flush immediately
            self.logger.info(f"✅ CSV file created and headers written: {self.csv_filename}")
        except Exception as e:
            self.logger.error(f"❌ Failed to initialize CSV: {e}")

    def write_to_csv(self, item):
        """Write item to CSV immediately with flush"""
        try:
            if self.csv_writer:
                row = {field: item.get(field, '') or '' for field in self.csv_headers}
                self.csv_writer.writerow(row)
                self.csv_file.flush()  # CRITICAL: Flush immediately after each write
                self.logger.info(f"              💾 ✅ WRITTEN TO CSV: {item.get('Name', 'Unknown')}")
                return True
            else:
                self.logger.error(f"              ❌ CSV writer not initialized")
                return False
        except Exception as e:
            self.logger.error(f"              ❌ Failed to write to CSV: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
            return False

    def fix_chromedriver_cache(self):
        """Fix ChromeDriver version mismatch"""
        try:
            import shutil
            import os

            # Get Chrome version
            try:
                chrome_version_output = subprocess.check_output(
                    ['google-chrome', '--version'],
                    stderr=subprocess.DEVNULL
                ).decode('utf-8').strip()

                self.logger.info(f"  🌐 Detected: {chrome_version_output}")

                chrome_version_full = chrome_version_output.split()[2]
                chrome_major = chrome_version_full.split('.')[0]
                self.chrome_version = int(chrome_major)

                os.environ['CHROME_VERSION_OVERRIDE'] = str(self.chrome_version)
                self.logger.info(f"  📌 ChromeDriver version: {self.chrome_version}")

            except Exception as e:
                self.logger.warning(f"  ⚠️  Could not detect Chrome version: {e}")
                self.chrome_version = None

        except Exception as e:
            self.logger.warning(f"  ⚠️  Could not fix ChromeDriver cache: {e}")

    def load_discovered_urls(self):
        """Load discovered URLs from JSON file (optional)"""
        try:
            project_root = Path(__file__).parent.parent.parent.parent
            json_files = sorted(project_root.glob("discovered_urls_*.json"), reverse=True)

            if json_files:
                json_file = json_files[0]
                self.logger.info(f"📂 Loading discovered URLs from: {json_file}")

                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                self.logger.info(f"   ✅ Loaded {len(data['categories'])} categories")
                return data['categories']
        except:
            pass

        return {}

    def build_start_urls(self):
        """Build start URLs - Postpaid + Visitor only"""
        urls = [
            # VISITOR LINE (1 URL)
            {
                'url': 'https://www.etisalat.ae/en/c/mobile/plans/visitor-line.html',
                'main_group': 'Mobile Plans',
                'group': 'Visitor',
                'subcat_name': 'Visitor Line',
                'navigational_aid': 'Mobile Plans > Visitor > Visitor Line',
                'category_key': 'mobile_visitor',
            },

            # POSTPAID (5 URLs)
            {
                'url': 'https://www.etisalat.ae/b2c/heshop/plans/postpaid-plans?subCategory=cat1970015&category=cat1970016&lang=en',
                'main_group': 'Mobile Plans',
                'group': 'Postpaid',
                'subcat_name': 'Freedom Entertainment Plans',
                'navigational_aid': 'Mobile Plans > Postpaid > Freedom Entertainment Plans',
                'category_key': 'mobile_postpaid',
            },
            {
                'url': 'https://www.etisalat.ae/b2c/heshop/plans/postpaid-plans?subCategory=cat1970015&category=cat1970017&lang=en',
                'main_group': 'Mobile Plans',
                'group': 'Postpaid',
                'subcat_name': 'Freedom Endless Data Plans',
                'navigational_aid': 'Mobile Plans > Postpaid > Freedom Endless Data Plans',
                'category_key': 'mobile_postpaid',
            },
            {
                'url': 'https://www.etisalat.ae/b2c/heshop/plans/postpaid-plans?subCategory=cat1970015&category=cat1970018&lang=en',
                'main_group': 'Mobile Plans',
                'group': 'Postpaid',
                'subcat_name': 'Freedom Unlimited Calling Plans',
                'navigational_aid': 'Mobile Plans > Postpaid > Freedom Unlimited Calling Plans',
                'category_key': 'mobile_postpaid',
            },
            {
                'url': 'https://www.etisalat.ae/b2c/heshop/plans/postpaid-plans?subCategory=cat1970015&category=cat1970019&lang=en',
                'main_group': 'Mobile Plans',
                'group': 'Postpaid',
                'subcat_name': 'Emirati Freedom',
                'navigational_aid': 'Mobile Plans > Postpaid > Emirati Freedom',
                'category_key': 'mobile_postpaid',
            },
            {
                'url': 'https://www.etisalat.ae/b2c/heshop/plans/postpaid-plans?subCategory=cat1970015&category=cat1970020&lang=en',
                'main_group': 'Mobile Plans',
                'group': 'Postpaid',
                'subcat_name': 'Freedom Standard Plans',
                'navigational_aid': 'Mobile Plans > Postpaid > Freedom Standard Plans',
                'category_key': 'mobile_postpaid',
            },
        ]

        self.logger.info(f"   📊 Total URLs: {len(urls)} (1 Visitor + 5 Postpaid)")
        return urls

    def start_requests(self):
        """Start requests from URLs"""
        for url_data in self.start_urls:
            meta = {
                'selenium': True,
                'main_group': url_data['main_group'],
                'group': url_data['group'],
                'subcat_name': url_data['subcat_name'],
                'navigational_aid': url_data.get('navigational_aid'),
                'category_key': url_data['category_key'],
            }

            self.logger.info(f"📥 Queuing: {url_data.get('navigational_aid', url_data['subcat_name'])}")

            yield scrapy.Request(
                url_data['url'],
                meta=meta,
                callback=self.parse,
                dont_filter=True,
                errback=self.errback_httpbin,
            )

    def errback_httpbin(self, failure):
        """Handle request failures"""
        self.logger.error(f"❌ Request failed: {failure.request.url}")
        self.logger.error(f"   Reason: {failure.value}")

    def parse(self, response):
        """Parse plan listing page"""
        self.pages_scraped += 1

        main_group = response.meta['main_group']
        group = response.meta['group']
        subcat_name = response.meta['subcat_name']
        breadcrumb = response.meta.get('navigational_aid') or f"{main_group} > {group} > {subcat_name}"

        self.logger.info(f"\n{'─'*100}")
        self.logger.info(f"[Page {self.pages_scraped}] {breadcrumb}")
        self.logger.info(f"              URL: {response.url}")
        self.logger.info(f"{'─'*100}")

        # Save page HTML for debugging
        debug_file = self.debug_dir / f"page_{self.pages_scraped}_{subcat_name.replace(' ', '_')}.html"
        debug_file.write_text(response.text, encoding='utf-8')

        # Check if Selenium driver is available
        driver = response.meta.get('selenium_driver')

        if driver:
            self.logger.info("              🌐 Using Selenium driver for extraction")
            time.sleep(2)

            # Detect page type
            view_plans_buttons = driver.find_elements(By.CSS_SELECTOR, 'a.btn.btn-eand-white.ripple-effect')
            view_plans_buttons = [btn for btn in view_plans_buttons if 'View Plans' in btn.text]

            if view_plans_buttons:
                self.logger.info("              📂 Page type: CATEGORY (has View Plans buttons)")
                yield from self.navigate_to_category_plans(driver, response, breadcrumb, main_group, group)
            else:
                self.logger.info("              📄 Page type: DIRECT PLANS")
                plans_on_this_page = 0
                for item in self.extract_with_selenium(driver, response, breadcrumb, main_group, group):
                    plans_on_this_page += 1
                    yield item

                self.logger.info(f"\n              📊 Page Summary: {plans_on_this_page} plans scraped")
        else:
            self.logger.warning("              ⚠️  No Selenium driver available")

        self.logger.info(f"\n              ✅ Total plans extracted: {self.plans_extracted}")
        self.logger.info(f"{'─'*100}\n")

    def get_category_from_url(self, url):
        """Extract category information from URL"""
        postpaid_match = re.search(r'category=(cat\d+)', url)
        if postpaid_match:
            cat_id = postpaid_match.group(1)
            return 'Mobile Plans', 'Postpaid', f'Postpaid {cat_id}'

        if 'visitor-line' in url:
            return 'Mobile Plans', 'Visitor', 'Visitor Line'
        elif 'prepaid' in url or 'wasel' in url:
            return 'Mobile Plans', 'Prepaid', 'Prepaid'

        return 'Mobile Plans', 'Unknown', 'Unknown'

    def navigate_to_category_plans(self, driver, response, breadcrumb, main_group, group):
        """Navigate through category pages with 'View Plans' buttons"""
        try:
            self.logger.info(f"\n              📂 Looking for 'View Plans' buttons...")
            time.sleep(3)

            view_plans_buttons = driver.find_elements(By.CSS_SELECTOR, 'a.btn.btn-eand-white.ripple-effect')
            view_plans_buttons = [btn for btn in view_plans_buttons if 'View Plans' in btn.text]

            self.logger.info(f"              🔍 Found {len(view_plans_buttons)} buttons")

            if not view_plans_buttons:
                return

            button_data = []
            for btn in view_plans_buttons:
                try:
                    href = btn.get_attribute('href')
                    text = btn.text.strip()
                    button_data.append({'href': href, 'text': text})
                except:
                    continue

            for i, btn_info in enumerate(button_data, 1):
                try:
                    self.logger.info(f"\n              ➡️  Category {i}/{len(button_data)}: {btn_info['text']}")

                    driver.get(btn_info['href'])
                    time.sleep(5)

                    new_main_group, new_group, new_subcat = self.get_category_from_url(driver.current_url)
                    category_breadcrumb = f"{new_main_group} > {new_group} > {new_subcat}"

                    yield from self.extract_with_selenium(driver, response, category_breadcrumb, new_main_group, new_group)

                    driver.back()
                    time.sleep(3)

                except Exception as e:
                    self.logger.error(f"              ❌ Error processing category {i}: {e}")
                    continue

        except Exception as e:
            self.logger.error(f"              ❌ Error navigating categories: {e}")

    def extract_with_selenium(self, driver, response, breadcrumb, main_group, group):
        """Extract data using Selenium"""
        try:
            time.sleep(5)

            plan_selectors = [
                '.v-card',
                '[class*="plan-card"]',
                'ion-card.eand-tariff-card',
            ]

            plans_scraped_on_page = 0
            swiper_iteration = 0
            processed_plan_identifiers = set()

            while True:
                swiper_iteration += 1
                self.logger.info(f"\n              🎯 Swiper iteration #{swiper_iteration}")

                plan_elements = []
                for selector in plan_selectors:
                    plan_elements = driver.find_elements(By.CSS_SELECTOR, selector)
                    if plan_elements:
                        self.logger.info(f"              🔍 Found {len(plan_elements)} visible plans")
                        break

                if not plan_elements:
                    break

                new_plans_in_iteration = 0

                for i, plan_elem in enumerate(plan_elements, 1):
                    try:
                        plan_html = plan_elem.get_attribute('outerHTML')
                        import hashlib
                        plan_identifier = hashlib.md5(plan_html.encode()).hexdigest()

                        if plan_identifier in processed_plan_identifiers:
                            continue

                        global_plan_num = plans_scraped_on_page + 1
                        self.logger.info(f"\n              📍 Processing plan #{global_plan_num}...")

                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", plan_elem)
                        time.sleep(2)

                        # Extract from outer card
                        commitment_outer = None
                        speed_outer = None
                        price_outer = None
                        promotion_outer = None

                        # Price
                        try:
                            price_elems = plan_elem.find_elements(By.CSS_SELECTOR, 'span.price')
                            for elem in price_elems:
                                text = driver.execute_script("return arguments[0].textContent;", elem).strip()
                                if 'AED' in text:
                                    price_outer = text
                                    self.logger.info(f"              ✓ Price: {price_outer}")
                                    break
                        except:
                            pass

                        # Commitment
                        try:
                            commitment_elems = plan_elem.find_elements(By.CSS_SELECTOR, 'div.contract-duration-container')
                            if commitment_elems:
                                commitment_outer = driver.execute_script("return arguments[0].textContent;", commitment_elems[0]).strip()
                                if commitment_outer:
                                    self.logger.info(f"              ✓ Commitment: {commitment_outer}")
                        except:
                            pass

                        # Find and click "More details"
                        more_details_btns = plan_elem.find_elements(By.CSS_SELECTOR, 'span.btn-underline')
                        more_details_btns = [btn for btn in more_details_btns if 'More details' in btn.text]

                        if not more_details_btns:
                            continue

                        self.logger.info(f"              🖱️  Clicking 'More details'...")

                        try:
                            more_details_btns[0].click()
                            time.sleep(1)
                        except:
                            try:
                                driver.execute_script("arguments[0].click();", more_details_btns[0])
                                time.sleep(1)
                            except Exception as e:
                                self.logger.error(f"              ❌ Could not click: {e}")
                                continue

                        # Extract from side panel
                        item = self.extract_from_more_details(driver, response, breadcrumb, main_group, group,
                                                             global_plan_num, commitment_outer, speed_outer,
                                                             promotion_outer, price_outer, category_url=response.url)

                        if item:
                            plan_name = item.get('Name', '')
                            if plan_name in self.processed_plans:
                                self.logger.info(f"              ⏭️  Duplicate: {plan_name}")
                                continue

                            self.processed_plans.add(plan_name)
                            self.plans_extracted += 1
                            plans_scraped_on_page += 1
                            new_plans_in_iteration += 1

                            group_lower = group.lower()
                            if 'prepaid' in group_lower:
                                self.plans_by_category['prepaid'] += 1
                            elif 'visitor' in group_lower:
                                self.plans_by_category['visitor'] += 1
                            elif 'postpaid' in group_lower:
                                self.plans_by_category['postpaid'] += 1

                            processed_plan_identifiers.add(plan_identifier)

                            self.logger.info(f"              ✅ Scraped plan #{plans_scraped_on_page}")

                            # WRITE TO CSV IMMEDIATELY
                            self.write_to_csv(item)

                            # Also yield for Scrapy
                            yield item

                        # Close side panel
                        self.close_side_panel(driver)

                    except Exception as e:
                        self.logger.error(f"              ❌ Error: {e}")
                        try:
                            self.close_side_panel(driver)
                        except:
                            pass
                        continue

                self.logger.info(f"\n              📊 Iteration complete: {new_plans_in_iteration} new plans")

                if new_plans_in_iteration == 0 and swiper_iteration > 1:
                    break

                # Check for next button
                try:
                    next_btns = driver.find_elements(By.CSS_SELECTOR, 'button.swiper-button-next')

                    next_btn = None
                    for btn in next_btns:
                        aria_disabled = btn.get_attribute('aria-disabled')
                        class_attr = btn.get_attribute('class') or ''

                        if aria_disabled != 'true' and 'swiper-button-disabled' not in class_attr:
                            next_btn = btn
                            break

                    if next_btn:
                        driver.execute_script("arguments[0].click();", next_btn)
                        time.sleep(3)
                        continue
                    else:
                        break

                except:
                    break

        except Exception as e:
            self.logger.error(f"              ❌ Selenium extraction error: {e}")

    def extract_from_more_details(self, driver, response, breadcrumb, main_group, group, plan_num,
                                 commitment_outer=None, speed_outer=None, promotion_outer=None, price_outer=None, category_url=None):
        """Extract from side panel"""
        try:
            self.logger.info(f"                 ⏳ Waiting for side panel...")
            try:
                WebDriverWait(driver, 30).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.plans-side-sheet'))
                )
            except TimeoutException:
                self.logger.error(f"                 ❌ Timeout waiting for side panel")
                return None

            time.sleep(3)

            # Initialize fields
            name = None
            price_actual = price_outer
            speed = speed_outer
            local_data = None
            roaming_data = None
            local_minutes = None
            minutes_category = None
            entertainment_packs_data = None
            entertainment_pack = None
            uae_wifi_hours = None
            additional_benefits_list = []
            promotion = promotion_outer
            commitment = commitment_outer

            # Extract name
            try:
                name_elem = driver.find_element(By.CSS_SELECTOR, 'ion-header ion-title')
                name = name_elem.text.strip()
                self.logger.info(f"                 ✓ Name: {name}")
            except:
                pass

            # Extract benefits
            benefit_divs = driver.find_elements(By.CSS_SELECTOR, 'div.mb-24')

            for div in benefit_divs:
                try:
                    value_elems = div.find_elements(By.CSS_SELECTOR, 'span.fw-bold')
                    if not value_elems:
                        continue

                    value = value_elems[0].text.strip()
                    full_text = div.text.strip()
                    description_text = full_text.replace(value, '').strip()
                    desc_lower = description_text.lower()

                    if 'local data' in desc_lower:
                        local_data = value
                    elif 'roaming data' in desc_lower:
                        roaming_data = value
                    elif 'local minutes' in desc_lower:
                        local_minutes = value
                        minutes_category = "Flexi (Local & Int'l)" if 'flexi' in desc_lower else "Local Only"
                    elif 'entertainment packs data' in desc_lower:
                        entertainment_packs_data = value
                    elif 'entertainment pack' in desc_lower:
                        entertainment_pack = value
                    elif 'wifi hours' in desc_lower:
                        uae_wifi_hours = value
                    elif 'speed' in desc_lower:
                        speed = value

                except:
                    continue

            # Create item
            item = EtisalatPlanItem()

            item['Link'] = category_url or response.url
            item['Name'] = name
            item['Price_Actual'] = price_actual
            item['Main_Group'] = main_group
            item['Group'] = group
            item['Navigational_Aid'] = breadcrumb
            item['Speed'] = speed
            item['Local_Data'] = local_data
            item['Roaming_Data'] = roaming_data
            item['Minutes'] = local_minutes
            item['Minutes_Category'] = minutes_category
            item['Variable'] = None
            item['Variable_value'] = None
            item['Entertainment_Packs_Data'] = entertainment_packs_data
            item['Entertainment_Pack'] = entertainment_pack
            item['UAE_WiFi_Hours'] = uae_wifi_hours
            item['Additional_Benefits'] = " | ".join(additional_benefits_list) if additional_benefits_list else None
            item['Promotion'] = promotion
            item['Commitment'] = commitment
            item['GTIN_Code'] = None
            item['UAE_GTIN'] = None
            item['EAN_Code'] = None
            item['url'] = response.url
            item['scrape_ts'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item['insert_ts'] = None
            item['frequency'] = "daily"
            item['domain'] = "etisalat.ae"

            return item

        except Exception as e:
            self.logger.error(f"                 ❌ Error extracting from side panel: {e}")
            return None

    def close_side_panel(self, driver):
        """Close side panel"""
        try:
            close_icons = driver.find_elements(By.CSS_SELECTOR, 'ion-icon[src*="close-black.svg"]')
            if close_icons:
                close_icons[0].click()
                time.sleep(1)
                return True
        except:
            pass

        try:
            from selenium.webdriver.common.keys import Keys
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
            time.sleep(1)
            return True
        except:
            pass

        return False

    def closed(self, reason):
        """Close CSV file and print final report"""
        if self.csv_file:
            try:
                self.csv_file.close()
                self.logger.info(f"✅ CSV file closed: {self.csv_filename}")
            except:
                pass

        report = f"""
{'='*100}
ETISALAT UAE COMPLETE SPIDER - FINAL REPORT
{'='*100}

📊 SCRAPING STATISTICS:
  Pages Scraped:          {self.pages_scraped}
  Plans Extracted:        {self.plans_extracted}

  By Category:
    • Visitor:            {self.plans_by_category['visitor']}
    • Postpaid:           {self.plans_by_category['postpaid']}

📁 OUTPUT:
  CSV File:               {self.csv_filename}

{'='*100}
"""

        self.logger.info(report)
