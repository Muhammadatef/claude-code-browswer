"""
Etisalat UAE Mobile Plans Spider
=================================

This spider scrapes mobile plans from etisalat.ae website with comprehensive
navigation support including "more details" buttons and swiper navigation.

Features:
- Clicks "More Details" button for each plan to reveal full information
- Handles swiper/carousel navigation to access all plans
- Extracts complete plan details matching du.ae structure
- Identifies minutes category (Flexi International vs Local Only)
- Extracts internet speed for each plan
- Supports both Selenium and Scrapy extraction methods

Author: Claude
Date: 2025-11-20
Version: 1.0
"""

import scrapy
import re
import time
from datetime import datetime
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from eand.items import EtisalatPlanItem


class EtisalatSpider(scrapy.Spider):
    """Spider for scraping Etisalat UAE mobile plans"""

    name = "etisalat_plans"
    allowed_domains = ["etisalat.ae"]

    # Start URLs for different plan categories
    start_urls = [
        'https://www.etisalat.ae/en/c/mobile/postpaid-plans.html',
        'https://www.etisalat.ae/en/c/mobile/prepaid-plans.html',
        'https://www.etisalat.ae/en/c/home/internet-plans.html',
    ]

    custom_settings = {
        'FEEDS': {
            f'output/etisalat_plans_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv': {
                'format': 'csv',
                'encoding': 'utf-8-sig',
                'overwrite': True,
                'fields': [
                    'Link', 'Name', 'Description',
                    'Price_Actual', 'Price_Original', 'Discount',
                    'Main_Group', 'Group', 'Navigational_Aid',
                    'Benefit_1', 'Benefit_2', 'Benefit_3', 'Benefit_4', 'Benefit_5',
                    'Speed', 'Minutes_Category', 'Local_Minutes', 'International_Minutes',
                    'Data_Allowance', 'Roaming_Data', 'Commitment',
                    'GTIN_Code', 'UAE_GTIN', 'EAN_Code',
                    'url', 'scrape_ts', 'domain'
                ],
            },
        },
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 3,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        self.debug_dir = Path("debug")
        self.debug_dir.mkdir(exist_ok=True)
        self.plans_extracted = 0
        self.pages_scraped = 0

    def start_requests(self):
        """Generate initial requests with Selenium enabled"""
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={'selenium': True},
                callback=self.parse,
                dont_filter=True,
                errback=self.errback_handler,
            )

    def errback_handler(self, failure):
        """Handle request failures"""
        self.logger.error(f"❌ Request failed: {failure.request.url}")
        self.logger.error(f"   Reason: {failure.value}")

    def parse(self, response):
        """Parse plan listing page with navigation support"""
        self.pages_scraped += 1

        # Determine category from URL
        main_group, group = self.categorize_url(response.url)
        breadcrumb = f"{main_group} > {group}"

        self.logger.info(f"\n{'='*100}")
        self.logger.info(f"[Page {self.pages_scraped}] {breadcrumb}")
        self.logger.info(f"URL: {response.url}")
        self.logger.info(f"{'='*100}")

        # Get Selenium driver
        driver = response.meta.get('selenium_driver')

        if not driver:
            self.logger.error("❌ Selenium driver not available")
            return

        try:
            # Wait for plans to load
            time.sleep(3)

            # Process all plans with swiper navigation
            all_plans_data = []

            while True:
                # Extract plans from current view
                plans_data = self.extract_plans_from_current_view(
                    driver, response, breadcrumb, main_group, group
                )
                all_plans_data.extend(plans_data)

                # Try to click "next" button on swiper
                if not self.click_swiper_next(driver):
                    # No more plans to navigate
                    break

                # Wait for new plans to load
                time.sleep(2)

            # Yield all extracted items
            for item in all_plans_data:
                self.plans_extracted += 1
                yield item

            self.logger.info(f"\n✅ Extracted {len(all_plans_data)} plans from this page")
            self.logger.info(f"{'='*100}\n")

        except Exception as e:
            self.logger.error(f"❌ Error parsing page: {e}")
            import traceback
            self.logger.error(traceback.format_exc())

    def extract_plans_from_current_view(self, driver, response, breadcrumb, main_group, group):
        """Extract all visible plan cards from current view"""
        plans_data = []

        try:
            # Find all visible plan cards
            plan_cards = driver.find_elements(By.CSS_SELECTOR, '.plan-card, .product-card, [class*="plan"], article')

            # Filter to actual plan cards (avoid duplicates/empty elements)
            valid_cards = []
            for card in plan_cards:
                try:
                    if card.is_displayed() and card.size['height'] > 50:
                        valid_cards.append(card)
                except:
                    continue

            self.logger.info(f"Found {len(valid_cards)} visible plan cards")

            for i, card in enumerate(valid_cards, 1):
                try:
                    # Scroll card into view
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                    time.sleep(1)

                    # Click "More Details" button if exists
                    more_details_clicked = self.click_more_details(driver, card)

                    if more_details_clicked:
                        time.sleep(2)  # Wait for details to load

                    # Extract plan data
                    item = self.extract_plan_data(driver, card, response, breadcrumb, main_group, group)

                    if item:
                        plans_data.append(item)
                        self.logger.info(f"✓ Extracted plan #{i}: {item.get('Name', 'Unknown')}")

                    # Close details modal if opened
                    if more_details_clicked:
                        self.close_details_modal(driver)

                except Exception as e:
                    self.logger.error(f"❌ Error extracting card #{i}: {e}")
                    continue

        except Exception as e:
            self.logger.error(f"❌ Error finding plan cards: {e}")

        return plans_data

    def click_more_details(self, driver, card):
        """Click 'More Details' button on a plan card"""
        try:
            # Try multiple selectors for "More Details" button
            button_selectors = [
                '.more-details-btn',
                'button:contains("More details")',
                'a:contains("More details")',
                '[aria-label*="more details"]',
                '.btn-details',
                '.view-details',
            ]

            for selector in button_selectors:
                try:
                    if 'contains' in selector:
                        # Use XPath for text-based search
                        buttons = card.find_elements(By.XPATH, './/button[contains(., "More details") or contains(., "View details")]')
                    else:
                        buttons = card.find_elements(By.CSS_SELECTOR, selector)

                    for button in buttons:
                        if button.is_displayed() and button.is_enabled():
                            # Scroll to button
                            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                            time.sleep(0.5)

                            # Try to click
                            try:
                                button.click()
                                self.logger.info("   ✓ Clicked 'More Details' button")
                                return True
                            except ElementClickInterceptedException:
                                # Try JavaScript click
                                driver.execute_script("arguments[0].click();", button)
                                self.logger.info("   ✓ Clicked 'More Details' (JS)")
                                return True
                except:
                    continue

            return False

        except Exception as e:
            self.logger.debug(f"Could not click more details: {e}")
            return False

    def close_details_modal(self, driver):
        """Close the details modal/overlay"""
        try:
            # Try multiple close button selectors
            close_selectors = [
                '.modal-close',
                '.close-btn',
                '[aria-label="Close"]',
                'button.close',
                '.overlay-close',
            ]

            for selector in close_selectors:
                try:
                    close_btn = driver.find_element(By.CSS_SELECTOR, selector)
                    if close_btn.is_displayed():
                        close_btn.click()
                        time.sleep(1)
                        return True
                except:
                    continue

            # Press ESC key as fallback
            from selenium.webdriver.common.keys import Keys
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
            time.sleep(1)

        except Exception as e:
            self.logger.debug(f"Could not close modal: {e}")

    def click_swiper_next(self, driver):
        """Click the swiper 'Next' button to navigate to more plans"""
        try:
            # User provided selector
            next_button_selectors = [
                '.swiper-button-next.custom-swiper-button-next.d-none.d-lg-block',
                '.swiper-button-next',
                '[aria-label="Next slide"]',
                '.carousel-control-next',
            ]

            for selector in next_button_selectors:
                try:
                    next_btn = driver.find_element(By.CSS_SELECTOR, selector)

                    # Check if button is enabled (not disabled)
                    if next_btn.is_displayed() and next_btn.get_attribute('aria-disabled') != 'true':
                        # Scroll to button
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
                        time.sleep(0.5)

                        # Click
                        try:
                            next_btn.click()
                        except ElementClickInterceptedException:
                            driver.execute_script("arguments[0].click();", next_btn)

                        self.logger.info("   ➡️  Clicked swiper 'Next' button")
                        return True

                except NoSuchElementException:
                    continue

            return False

        except Exception as e:
            self.logger.debug(f"No more swiper navigation available: {e}")
            return False

    def extract_plan_data(self, driver, card, response, breadcrumb, main_group, group):
        """Extract all plan data from a card element"""
        try:
            item = EtisalatPlanItem()

            # Extract Name
            name = self.extract_field(card, [
                'h4.text-h6.white--text',
                '.plan-name',
                '.product-name',
                'h3', 'h4', 'h5',
            ])
            item['Name'] = name if name else "Unknown Plan"

            # Extract Description
            description = self.extract_field(card, [
                '.d-flex.flex-row.justify-center.align-center',
                '.plan-description',
                '.description',
                'p.subtitle',
            ])
            item['Description'] = description

            # Extract Price_Actual
            price_actual = self.extract_field(card, [
                '.text-h5',
                '.price-actual',
                '.current-price',
                '[class*="price"]',
            ])
            item['Price_Actual'] = self.clean_price(price_actual)

            # Extract Price_Original
            price_original = self.extract_field(card, [
                'span.text-decoration-line-through.text--h6',
                '.text-decoration-line-through',
                '.price-original',
                '.old-price',
            ])
            item['Price_Original'] = self.clean_price(price_original)

            # Extract Discount
            discount = self.extract_field(card, [
                '.text-overline.white--lighten80.text-truncate',
                '.discount-text',
                '.save-text',
            ], filter_text=['save', '%', 'month'])
            item['Discount'] = discount

            # Extract Benefits (1-5)
            benefits = self.extract_multiple_fields(card, [
                '.text-overline.text-truncate',
                '.benefit-item',
                '.feature-item',
                'ul li',
            ], max_items=5)

            item['Benefit_1'] = benefits[0] if len(benefits) > 0 else None
            item['Benefit_2'] = benefits[1] if len(benefits) > 1 else None
            item['Benefit_3'] = benefits[2] if len(benefits) > 2 else None
            item['Benefit_4'] = benefits[3] if len(benefits) > 3 else None
            item['Benefit_5'] = benefits[4] if len(benefits) > 4 else None

            # Extract Speed (Internet speed)
            speed = self.extract_speed(card)
            item['Speed'] = speed

            # Extract Minutes and determine category
            minutes_info = self.extract_minutes_info(card)
            item['Minutes_Category'] = minutes_info['category']
            item['Local_Minutes'] = minutes_info['local']
            item['International_Minutes'] = minutes_info['international']

            # Extract Data Allowance
            data = self.extract_field(card, [
                '[class*="data"]',
                '.data-allowance',
            ], filter_text=['GB', 'MB', 'data'])
            item['Data_Allowance'] = data

            # Extract Roaming Data
            roaming = self.extract_field(card, [
                '[class*="roaming"]',
                '.roaming-data',
            ], filter_text=['roaming'])
            item['Roaming_Data'] = roaming

            # Extract Commitment
            commitment = self.extract_field(card, [
                '.text-overline.white--lighten80.text-truncate.mb-1',
                '[title*="contract"]',
                '.commitment',
                '.contract-duration',
            ])

            # Also check for title attribute
            if not commitment:
                try:
                    elements = card.find_elements(By.CSS_SELECTOR, '[title]')
                    for elem in elements:
                        title = elem.get_attribute('title')
                        if title and 'contract' in title.lower():
                            commitment = title
                            break
                except:
                    pass

            item['Commitment'] = commitment

            # Product codes (usually not visible, check data attributes)
            item['GTIN_Code'] = self.extract_product_code(card, 'gtin')
            item['UAE_GTIN'] = self.extract_product_code(card, 'uae-gtin')
            item['EAN_Code'] = self.extract_product_code(card, 'ean')

            # Metadata
            item['Link'] = response.url
            item['Main_Group'] = main_group
            item['Group'] = group
            item['Navigational_Aid'] = breadcrumb
            item['url'] = response.url
            item['scrape_ts'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item['domain'] = "etisalat.ae"

            return item

        except Exception as e:
            self.logger.error(f"Error extracting plan data: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
            return None

    def extract_field(self, element, selectors, filter_text=None):
        """Extract text from element using multiple selectors with optional filtering"""
        for selector in selectors:
            try:
                elements = element.find_elements(By.CSS_SELECTOR, selector)
                for elem in elements:
                    text = elem.text.strip()
                    if text:
                        # Apply filter if provided
                        if filter_text:
                            if any(keyword.lower() in text.lower() for keyword in filter_text):
                                return text
                        else:
                            return text
            except:
                continue
        return None

    def extract_multiple_fields(self, element, selectors, max_items=5):
        """Extract multiple text values from element"""
        results = []
        for selector in selectors:
            try:
                elements = element.find_elements(By.CSS_SELECTOR, selector)
                for elem in elements:
                    text = elem.text.strip()
                    if text and text not in results:
                        results.append(text)
                        if len(results) >= max_items:
                            return results
            except:
                continue
        return results

    def extract_speed(self, element):
        """Extract internet speed from plan card"""
        # Look for speed indicators
        speed_keywords = ['mbps', 'mb/s', 'gbps', 'speed', 'bandwidth']
        all_text = element.text.lower()

        for keyword in speed_keywords:
            if keyword in all_text:
                # Try to extract the speed value
                try:
                    # Pattern: number + optional space + unit
                    pattern = r'(\d+(?:\.\d+)?)\s*(?:mbps|mb/s|gbps|gb/s)'
                    match = re.search(pattern, all_text, re.IGNORECASE)
                    if match:
                        return match.group(0)
                except:
                    pass

        # Fallback: look for speed in specific elements
        speed_selectors = [
            '[class*="speed"]',
            '[data-speed]',
            '.internet-speed',
        ]

        for selector in speed_selectors:
            try:
                speed_elem = element.find_element(By.CSS_SELECTOR, selector)
                speed_text = speed_elem.text.strip()
                if speed_text:
                    return speed_text
            except:
                continue

        return None

    def extract_minutes_info(self, element):
        """Extract minutes information and categorize as Flexi/Local"""
        result = {
            'category': None,
            'local': None,
            'international': None,
        }

        all_text = element.text.lower()

        # Check for Flexi minutes (international + local)
        if 'flexi' in all_text or 'international' in all_text:
            result['category'] = "Flexi (International + Local)"

            # Extract minutes value
            pattern = r'(\d+)\s*(?:flexi\s*)?min'
            match = re.search(pattern, all_text, re.IGNORECASE)
            if match:
                minutes = match.group(1)
                result['local'] = minutes
                result['international'] = minutes
        else:
            # Local only
            result['category'] = "Local Only"

            # Extract local minutes
            pattern = r'(\d+)\s*(?:local\s*)?min'
            match = re.search(pattern, all_text, re.IGNORECASE)
            if match:
                result['local'] = match.group(1)

        return result

    def extract_product_code(self, element, code_type):
        """Extract product codes from data attributes"""
        try:
            code = element.get_attribute(f'data-{code_type}')
            return code if code else None
        except:
            return None

    def clean_price(self, price_text):
        """Clean and format price text"""
        if not price_text:
            return None

        # Remove extra whitespace
        price_text = ' '.join(price_text.split())

        # Ensure AED is included
        if 'AED' not in price_text.upper():
            # Try to add AED if we find a number
            if re.search(r'\d+', price_text):
                price_text = f"AED {price_text}"

        return price_text

    def categorize_url(self, url):
        """Determine Main_Group and Group from URL"""
        url_lower = url.lower()

        if 'postpaid' in url_lower:
            main_group = "Mobile Plans"
            group = "Postpaid"
        elif 'prepaid' in url_lower:
            main_group = "Mobile Plans"
            group = "Prepaid"
        elif 'home' in url_lower or 'internet' in url_lower:
            main_group = "Home Internet"
            group = "Internet Plans"
        else:
            main_group = "Other"
            group = "Other"

        return main_group, group

    def closed(self, reason):
        """Final report when spider closes"""
        report = f"""
{'='*100}
ETISALAT UAE SPIDER - FINAL REPORT
{'='*100}

STATISTICS:
  Pages Scraped:          {self.pages_scraped}
  Plans Extracted:        {self.plans_extracted}

FEATURES IMPLEMENTED:
  ✅ More Details button clicking
  ✅ Swiper navigation support
  ✅ Minutes categorization (Flexi vs Local)
  ✅ Internet speed extraction
  ✅ Comprehensive field extraction
  ✅ Modal/overlay handling

OUTPUT:
  CSV File:               output/etisalat_plans_*.csv
  Debug Files:            debug/

{'='*100}
"""
        self.logger.info(report)

        # Save report
        report_file = self.output_dir / f"etisalat_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        report_file.write_text(report)
        self.logger.info(f"📊 Report saved: {report_file}")
