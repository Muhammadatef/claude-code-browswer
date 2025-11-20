"""
Selenium Middleware for Etisalat Scraper

This middleware integrates Selenium WebDriver with Scrapy to handle
JavaScript-heavy pages and dynamic content.
"""

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


class SeleniumMiddleware:
    """Middleware to handle requests using Selenium WebDriver"""

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(middleware.spider_closed, signal=signals.spider_closed)
        return middleware

    def spider_opened(self, spider):
        """Initialize Selenium WebDriver when spider opens"""
        spider.logger.info("Initializing Selenium WebDriver...")

        chrome_options = Options()

        # Run in headless mode for production (set to False for debugging)
        headless = getattr(spider, 'headless', True)
        if headless:
            chrome_options.add_argument('--headless=new')

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        # Disable images and CSS for faster loading (optional)
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)

        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            spider.logger.info("✅ Selenium WebDriver initialized successfully")
        except Exception as e:
            spider.logger.error(f"❌ Failed to initialize Selenium: {e}")
            self.driver = None

    def spider_closed(self, spider):
        """Clean up Selenium WebDriver when spider closes"""
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
            spider.logger.info("Selenium WebDriver closed")

    def process_request(self, request, spider):
        """Process requests that need Selenium"""

        # Only process requests marked with 'selenium' meta
        if not request.meta.get('selenium'):
            return None

        if not hasattr(self, 'driver') or not self.driver:
            spider.logger.error("Selenium driver not available")
            return None

        try:
            spider.logger.info(f"Loading page with Selenium: {request.url}")

            self.driver.get(request.url)

            # Wait for page to load
            time.sleep(3)

            # Wait for specific element if provided
            wait_selector = request.meta.get('wait_selector')
            if wait_selector:
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, wait_selector))
                    )
                except Exception as e:
                    spider.logger.warning(f"Wait selector '{wait_selector}' not found: {e}")

            # Get page source and create response
            body = self.driver.page_source.encode('utf-8')

            # Pass the driver to the spider via meta
            response = HtmlResponse(
                url=self.driver.current_url,
                body=body,
                encoding='utf-8',
                request=request
            )

            # Attach driver to response meta for use in spider
            response.meta['selenium_driver'] = self.driver

            return response

        except Exception as e:
            spider.logger.error(f"Error processing request with Selenium: {e}")
            return None
