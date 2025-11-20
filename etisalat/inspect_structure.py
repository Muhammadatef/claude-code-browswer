"""
Etisalat Page Inspector
=======================

This script loads the Etisalat plans page using Selenium and extracts
the HTML structure, CSS classes, and outerHTML for each data field.

It will generate a detailed report showing how to extract each column.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json


def inspect_etisalat_structure():
    """Inspect Etisalat page structure and extract element details"""

    print("\n" + "="*100)
    print("ETISALAT PAGE STRUCTURE INSPECTOR")
    print("="*100 + "\n")

    # Setup Chrome options
    chrome_options = Options()
    # chrome_options.add_argument('--headless=new')  # Comment out to see browser
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920,1080')

    # Initialize driver
    print("🌐 Initializing Chrome WebDriver...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Load the page
        url = "https://www.etisalat.ae/en/c/mobile/postpaid-plans.html"
        print(f"📥 Loading: {url}")
        driver.get(url)

        # Wait for page to load
        time.sleep(5)
        print("✅ Page loaded\n")

        # Find plan cards with multiple selectors
        print("🔍 Searching for plan cards...\n")

        card_selectors = [
            'ion-card',
            '.plan-card',
            '.product-card',
            '[class*="tariff-card"]',
            '[class*="plan"]',
            'article',
        ]

        plan_cards = []
        used_selector = None

        for selector in card_selectors:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            if elements and len(elements) > 0:
                # Filter to valid cards (has text content)
                valid_cards = [e for e in elements if len(e.text.strip()) > 50]
                if valid_cards:
                    plan_cards = valid_cards
                    used_selector = selector
                    print(f"✅ Found {len(plan_cards)} plan cards using selector: {selector}\n")
                    break

        if not plan_cards:
            print("❌ No plan cards found!")
            print("\n📋 Available classes on page:")
            all_classes = driver.execute_script("""
                return Array.from(document.querySelectorAll('[class]'))
                    .flatMap(el => Array.from(el.classList))
                    .filter((v, i, a) => a.indexOf(v) === i)
                    .slice(0, 50);
            """)
            for cls in all_classes:
                print(f"  - {cls}")
            return

        # Analyze first plan card in detail
        print("="*100)
        print("DETAILED ANALYSIS OF FIRST PLAN CARD")
        print("="*100 + "\n")

        card = plan_cards[0]

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
        time.sleep(1)

        # Card container info
        print("1. PLAN CARD CONTAINER")
        print("-" * 50)
        card_class = card.get_attribute('class')
        card_html_preview = card.get_attribute('outerHTML')[:200]
        print(f"   Element: {card.tag_name}")
        print(f"   Classes: {card_class}")
        print(f"   outerHTML preview: {card_html_preview}...\n")

        # Define extraction patterns
        extraction_patterns = {
            'Name': [
                'h4.text-h6.white--text',
                'ion-card-title.title',
                '.plan-name',
                'h3', 'h4', 'h5',
            ],
            'Description': [
                '.d-flex.flex-row.justify-center.align-center',
                '.plan-description',
                '.eand-badge__container',
                '[class*="description"]',
            ],
            'Price_Actual': [
                '.text-h5',
                '.eand-tariff-card__price-wrapper',
                '.price-actual',
                '[class*="price"]',
            ],
            'Price_Original': [
                'span.text-decoration-line-through.text--h6',
                '.text-decoration-line-through',
                '.price-original',
            ],
            'Discount': [
                '.text-overline.white--lighten80.text-truncate',
                '.promotion-container',
                '[class*="discount"]',
                '[class*="save"]',
            ],
            'Benefits': [
                '.text-overline.text-truncate',
                '.eand-tariff-card-body div',
                'ul li',
                '.benefit-item',
            ],
            'Speed': [
                '[class*="speed"]',
                '.internet-speed',
            ],
            'Minutes': [
                '[class*="minutes"]',
                '[class*="flexi"]',
            ],
            'Data_Allowance': [
                '[class*="data"]',
                '.data-allowance',
            ],
            'Roaming': [
                '[class*="roaming"]',
            ],
            'Commitment': [
                '.text-overline.white--lighten80.text-truncate.mb-1',
                '[title*="contract"]',
                '.contract-duration-container',
            ],
            'More_Details_Button': [
                'button[aria-label*="detail"]',
                '.more-details',
                'button:contains("More")',
            ],
        }

        results = {}

        # Extract each field
        for field_name, selectors in extraction_patterns.items():
            print(f"\n{len(results) + 2}. {field_name.upper().replace('_', ' ')}")
            print("-" * 50)

            found = False
            for selector in selectors:
                try:
                    elements = card.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        for i, elem in enumerate(elements[:3]):  # Show first 3 matches
                            try:
                                if elem.is_displayed():
                                    text = elem.text.strip()
                                    if text and len(text) > 0:
                                        elem_class = elem.get_attribute('class')
                                        elem_html = elem.get_attribute('outerHTML')

                                        # Limit HTML preview
                                        if len(elem_html) > 300:
                                            elem_html = elem_html[:300] + "..."

                                        print(f"   ✅ Selector: {selector}")
                                        print(f"   Element: {elem.tag_name}")
                                        print(f"   Classes: {elem_class}")
                                        print(f"   Text: {text[:100]}")
                                        print(f"   outerHTML: {elem_html}")

                                        if i < len(elements) - 1 and i < 2:
                                            print(f"\n   Alternative {i+2}:")

                                        found = True

                                        results[field_name] = {
                                            'selector': selector,
                                            'element': elem.tag_name,
                                            'classes': elem_class,
                                            'sample_text': text[:100],
                                            'outerHTML': elem_html,
                                        }

                                        if field_name not in ['Benefits', 'Description']:
                                            break  # Only show first match for single-value fields
                            except:
                                continue
                        if found:
                            break
                except:
                    continue

            if not found:
                print(f"   ⚠️  No elements found for {field_name}")

        # Try to find and click "More Details" button
        print("\n\n" + "="*100)
        print("TESTING 'MORE DETAILS' BUTTON")
        print("="*100 + "\n")

        more_details_selectors = [
            'button[aria-label*="More"]',
            'button[aria-label*="detail"]',
            '.more-details',
            'button.btn-primary',
            'a[href*="#"]',
        ]

        for selector in more_details_selectors:
            try:
                buttons = card.find_elements(By.CSS_SELECTOR, selector)
                for btn in buttons:
                    if btn.is_displayed():
                        btn_text = btn.text.strip().lower()
                        if 'more' in btn_text or 'detail' in btn_text or 'view' in btn_text:
                            print(f"✅ Found button:")
                            print(f"   Selector: {selector}")
                            print(f"   Text: {btn.text}")
                            print(f"   Classes: {btn.get_attribute('class')}")
                            print(f"   aria-label: {btn.get_attribute('aria-label')}")

                            # Try to click
                            print(f"\n🖱️  Attempting to click...")
                            try:
                                btn.click()
                                time.sleep(2)
                                print("✅ Button clicked successfully!")

                                # Check for modal/overlay
                                modal_selectors = ['.modal', '.overlay', '[role="dialog"]', '.details-panel']
                                for modal_sel in modal_selectors:
                                    modals = driver.find_elements(By.CSS_SELECTOR, modal_sel)
                                    if modals:
                                        print(f"\n📋 Modal/Overlay opened:")
                                        print(f"   Selector: {modal_sel}")
                                        print(f"   Classes: {modals[0].get_attribute('class')}")
                                break
                            except Exception as click_err:
                                print(f"⚠️  Could not click: {click_err}")
            except:
                continue

        # Look for swiper buttons
        print("\n\n" + "="*100)
        print("TESTING SWIPER/CAROUSEL NAVIGATION")
        print("="*100 + "\n")

        swiper_selectors = [
            '.swiper-button-next',
            '.swiper-button-next.custom-swiper-button-next',
            '[aria-label="Next slide"]',
            '.carousel-control-next',
        ]

        for selector in swiper_selectors:
            try:
                btns = driver.find_elements(By.CSS_SELECTOR, selector)
                if btns:
                    for btn in btns:
                        if btn.is_displayed():
                            print(f"✅ Found swiper button:")
                            print(f"   Selector: {selector}")
                            print(f"   Classes: {btn.get_attribute('class')}")
                            print(f"   aria-label: {btn.get_attribute('aria-label')}")
                            print(f"   aria-disabled: {btn.get_attribute('aria-disabled')}")
                            print(f"   outerHTML: {btn.get_attribute('outerHTML')[:200]}...")
                            break
            except:
                continue

        # Save results to JSON
        print("\n\n" + "="*100)
        print("SAVING RESULTS")
        print("="*100 + "\n")

        output_file = "etisalat/etisalat_structure_analysis.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"✅ Results saved to: {output_file}")

        # Save page HTML
        html_file = "etisalat/debug/etisalat_page.html"
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        print(f"✅ Page HTML saved to: {html_file}")

        # Save screenshot
        screenshot_file = "etisalat/debug/etisalat_page.png"
        driver.save_screenshot(screenshot_file)
        print(f"✅ Screenshot saved to: {screenshot_file}")

        print("\n" + "="*100)
        print("INSPECTION COMPLETE!")
        print("="*100 + "\n")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

    finally:
        driver.quit()
        print("🔚 Browser closed")


if __name__ == "__main__":
    inspect_etisalat_structure()
