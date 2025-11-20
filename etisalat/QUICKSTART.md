# Quick Start Guide - Etisalat Scraper

## Installation & Running (5 Minutes)

### Step 1: Install Dependencies

```bash
cd etisalat
pip install -r requirements.txt
```

### Step 2: Run the Spider

```bash
scrapy crawl etisalat_plans
```

### Step 3: View Results

```bash
# CSV file will be in output/ folder
ls -lh output/

# View the data
cat output/etisalat_plans_*.csv
```

## Key Features Implemented

### ✅ Navigation
- **More Details Button**: Automatically clicks to reveal full plan information
- **Swiper Navigation**: Clicks "Next" button to access all plans in carousel
- **Modal Handling**: Opens and closes detail overlays automatically

### ✅ Data Extraction (Matching du.ae Structure)

| Field | Source | Example |
|-------|--------|---------|
| Name | `h4.text-h6.white--text` | "Power Plan 125" |
| Description | `.d-flex.flex-row.justify-center.align-center` | "Calling" |
| Price_Actual | `.text-h5` | "AED 94" |
| Price_Original | `.text-decoration-line-through` | "AED 125" |
| Discount | `.text-overline.white--lighten80` | "Save 25% for 3 months" |
| Main_Group | URL-based | "Postpaid plans" |
| Group | `.v-tab.v-tab--active` | "Power Plans" |
| Benefits (1-5) | `.text-overline.text-truncate` | "13 GB", "Carry-over data", etc. |
| Speed | Pattern matching | "100 Mbps" |
| Minutes_Category | Content analysis | "Flexi (International + Local)" or "Local Only" |
| Commitment | `.text-overline.white--lighten80.text-truncate.mb-1[title]` | "12-month contract" |

### ✅ Special Features

1. **Minutes Categorization**
   - Detects "Flexi minutes" → "Flexi (International + Local)"
   - Regular minutes → "Local Only"
   - Extracts both local and international minute values

2. **Internet Speed Extraction**
   - Searches for speed patterns (Mbps, GB/s)
   - Checks multiple locations in the plan card
   - Returns formatted speed string

3. **Swiper Navigation**
   - Selector: `.swiper-button-next.custom-swiper-button-next.d-none.d-lg-block`
   - Checks if button is enabled before clicking
   - Waits for new content to load after navigation

## Debug Mode

To see the browser in action:

```bash
# Edit eand/middlewares.py and change:
headless = getattr(spider, 'headless', False)  # Change True to False
```

Or run with spider attribute:

```bash
scrapy crawl etisalat_plans -a headless=False
```

## Output Format

The CSV contains all fields matching du.ae structure:

```
Link,Name,Description,Price_Actual,Price_Original,Discount,Main_Group,Group,
Benefit_1,Benefit_2,Benefit_3,Benefit_4,Benefit_5,Speed,Minutes_Category,
Local_Minutes,International_Minutes,Data_Allowance,Roaming_Data,Commitment,
GTIN_Code,UAE_GTIN,EAN_Code,url,scrape_ts,domain
```

## Troubleshooting

### Issue: No plans extracted
- **Solution**: Check if website structure changed, run with `headless=False`

### Issue: ChromeDriver error
- **Solution**: `pip install --upgrade webdriver-manager selenium`

### Issue: Timeout errors
- **Solution**: Increase delays in `settings.py` (`DOWNLOAD_DELAY = 5`)

## Next Steps

- Verify extracted data matches requirements
- Add more URLs to `start_urls` if needed
- Customize field extraction in `etisalat_spider.py`
- Schedule regular scraping runs

## Contact

For issues or questions, refer to the main README.md
