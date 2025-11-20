"""
Scrapy Settings for Etisalat UAE Plans Scraper

For more information on Scrapy settings:
https://docs.scrapy.org/en/latest/topics/settings.html
"""

BOT_NAME = 'eand'

SPIDER_MODULES = ['eand.spiders']
NEWSPIDER_MODULE = 'eand.spiders'

# Crawl responsibly by identifying yourself
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website
DOWNLOAD_DELAY = 3
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'eand.middlewares.SeleniumMiddleware': 800,
}

# Configure item pipelines
# ITEM_PIPELINES = {
#    'eand.pipelines.EandPipeline': 300,
# }

# Enable and configure the AutoThrottle extension
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received
AUTOTHROTTLE_DEBUG = False

# Enable HTTP caching
HTTPCACHE_ENABLED = False

# Set settings whose default value is deprecated
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

# Log level
LOG_LEVEL = 'INFO'
