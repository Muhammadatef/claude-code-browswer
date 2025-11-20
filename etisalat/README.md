# Etisalat UAE Mobile Plans Scraper

This is a comprehensive web scraper for extracting mobile plan data from etisalat.ae using Scrapy and Selenium.

## Features

- ✅ **Automated Navigation**: Clicks "More Details" buttons and navigates through swiper/carousel
- ✅ **Complete Data Extraction**: Extracts all plan details matching du.ae structure
- ✅ **Minutes Categorization**: Identifies Flexi (International + Local) vs Local Only minutes
- ✅ **Internet Speed**: Extracts internet speed for each plan
- ✅ **Dynamic Content Handling**: Uses Selenium for JavaScript-heavy pages
- ✅ **Multiple Plan Categories**: Postpaid, Prepaid, and Home Internet

## Installation

### 1. Install Python Dependencies

```bash
cd etisalat
pip install -r requirements.txt
```

### 2. Install Chrome Browser

Make sure Google Chrome is installed on your system. The ChromeDriver will be installed automatically via webdriver-manager.

## Usage

### Run the Spider

```bash
cd etisalat
scrapy crawl etisalat_plans
```

### Run with Custom Settings

```bash
# Run in visible browser mode (for debugging)
scrapy crawl etisalat_plans -s SELENIUM_HEADLESS=False

# Run with custom output file
scrapy crawl etisalat_plans -o custom_output.csv
```

## Output

The spider generates:

- **CSV File**: `output/etisalat_plans_YYYYMMDD_HHMMSS.csv`
- **Debug Files**: `debug/` folder (if errors occur)
- **Final Report**: `output/etisalat_report_YYYYMMDD_HHMMSS.txt`

## Data Fields

| Field | Description | Example |
|-------|-------------|---------|
| `Name` | Plan name | "Power Plan 125" |
| `Description` | Plan description | "Calling" |
| `Price_Actual` | Current price | "AED 94" |
| `Price_Original` | Original price (before discount) | "AED 125" |
| `Discount` | Discount information | "Save 25% for 3 months" |
| `Main_Group` | Category | "Mobile Plans" or "Home Internet" |
| `Group` | Subcategory | "Postpaid", "Prepaid", etc. |
| `Benefit_1` to `Benefit_5` | Plan benefits | "13 GB", "Carry-over data", etc. |
| `Speed` | Internet speed | "100 Mbps" |
| `Minutes_Category` | Type of minutes | "Flexi (International + Local)" or "Local Only" |
| `Local_Minutes` | Local calling minutes | "400" |
| `International_Minutes` | International minutes | "400" (if Flexi) |
| `Data_Allowance` | Data included | "13 GB" |
| `Roaming_Data` | Roaming data | "100 MB" |
| `Commitment` | Contract duration | "12-month contract" |
| `GTIN_Code` | Product GTIN code | (if available) |
| `UAE_GTIN` | UAE-specific GTIN | (if available) |
| `EAN_Code` | EAN code | (if available) |

## Navigation Features

### More Details Button
The spider automatically:
1. Scrolls each plan card into view
2. Clicks "More Details" button to reveal full information
3. Extracts all data from the expanded view
4. Closes the modal/overlay

### Swiper Navigation
The spider:
1. Extracts all visible plans on the current slide
2. Clicks the "Next" button (`.swiper-button-next`)
3. Waits for new plans to load
4. Repeats until all plans are scraped

## Configuration

### Spider Settings

Edit `eand/settings.py` to customize:

- `CONCURRENT_REQUESTS`: Number of concurrent requests (default: 1)
- `DOWNLOAD_DELAY`: Delay between requests (default: 3 seconds)
- `LOG_LEVEL`: Logging verbosity (default: INFO)

### Selenium Options

Edit `eand/middlewares.py` to customize browser behavior:

- `headless`: Run browser in headless mode (default: True)
- Window size, user agent, etc.

## Troubleshooting

### ChromeDriver Issues

If you encounter ChromeDriver version mismatch:

```bash
pip install --upgrade webdriver-manager
```

The middleware will automatically download the correct ChromeDriver version.

### No Plans Found

1. Check if the website structure has changed
2. Run with `headless=False` to see the browser
3. Check `debug/` folder for page HTML snapshots

### Slow Execution

- Increase `DOWNLOAD_DELAY` in settings.py
- Reduce number of `start_urls`
- Enable image/CSS blocking in middleware

## Project Structure

```
etisalat/
├── eand/
│   ├── __init__.py
│   ├── items.py              # Data models
│   ├── middlewares.py        # Selenium middleware
│   ├── settings.py           # Scrapy settings
│   └── spiders/
│       ├── __init__.py
│       └── etisalat_spider.py  # Main spider
├── output/                   # CSV output files
├── debug/                    # Debug files
├── requirements.txt          # Dependencies
├── scrapy.cfg                # Scrapy configuration
└── README.md                 # This file
```

## Development

### Adding New Fields

1. Add field to `items.py` (`EtisalatPlanItem`)
2. Add extraction logic in `etisalat_spider.py` (`extract_plan_data` method)
3. Add field to `custom_settings['FEEDS']['fields']` list

### Adding New URLs

Add URLs to `start_urls` list in `etisalat_spider.py`:

```python
start_urls = [
    'https://www.etisalat.ae/en/c/mobile/postpaid-plans.html',
    'https://www.etisalat.ae/en/c/your-new-category.html',  # Add here
]
```

## License

This project is for educational and research purposes only.

## Author

Created with Claude AI
Date: 2025-11-20
Version: 1.0
