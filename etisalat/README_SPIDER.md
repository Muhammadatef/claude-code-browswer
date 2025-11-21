# Etisalat UAE Complete Spider - Quick Start Guide

## ✅ What's Been Fixed

1. **Immediate CSV Writing**: Each scraped plan is written to CSV immediately (no batching)
2. **Complete Item Definition**: All fields properly defined in `items_selenium.py`
3. **Data Pipelines**: Cleaning, validation, and deduplication pipelines enabled
4. **Dedicated Output Folders**:
   - `etisalat_output/` - CSV files with immediate writes
   - `etisalat_debug/` - Debug HTML files

## 🚀 How to Run

### From the etisalat directory:

```bash
cd /home/user/claude-code-browswer/etisalat
scrapy crawl etisalat_complete
```

### What Happens:

1. **CSV file created immediately** in `etisalat_output/etisalat_complete_YYYYMMDD_HHMMSS.csv`
2. **Headers written** to CSV as soon as spider starts
3. **Each plan written immediately** to CSV after scraping (with flush)
4. **Debug HTML saved** for each page in `etisalat_debug/`

## 📊 Expected Output

- **Total URLs**: 6 (1 Visitor + 5 Postpaid)
- **Expected Plans**: ~70 plans
  - Visitor: ~7 plans
  - Postpaid: ~63 plans

## 📁 File Structure

```
etisalat/
├── eand/
│   ├── items_selenium.py          # Item definition with all fields
│   ├── pipelines.py                # Data cleaning and validation
│   ├── settings.py                 # Pipelines enabled
│   ├── middlewares.py              # Selenium middleware
│   └── spiders/
│       └── etisalat_complete_spider.py  # Main spider
├── etisalat_output/               # CSV files (created on first run)
│   └── etisalat_complete_*.csv
└── etisalat_debug/                # Debug HTML files (created on first run)
    └── page_*.html
```

## 🔍 Key Features

### Two-Stage Extraction:
1. **Outer Card** (before clicking "More details"):
   - Price
   - Commitment
   - Speed (conditional)
   - Promotion

2. **Side Panel** (after clicking "More details"):
   - Name
   - Local Data
   - Roaming Data
   - Minutes
   - Entertainment Packs
   - Additional Benefits

### CSV Fields:
```
Link, Name, Price_Actual, Main_Group, Group, Navigational_Aid,
Speed, Local_Data, Roaming_Data, Minutes, Minutes_Category,
Variable, Variable_value, Entertainment_Packs_Data,
Entertainment_Pack, UAE_WiFi_Hours, Additional_Benefits,
Promotion, Commitment, GTIN_Code, UAE_GTIN, EAN_Code,
scrape_ts, insert_ts, frequency, domain
```

## 🔧 Monitoring Progress

Watch the logs for these indicators:

```
✅ CSV file created and headers written: ...
💾 ✅ WRITTEN TO CSV: [Plan Name]
📍 Processing plan #1...
✅ Scraped plan #1
```

Each line with `💾 ✅ WRITTEN TO CSV` means a plan was successfully written to the CSV file.

## ⚠️ Important Notes

1. **No Batching**: Each plan is written immediately with `flush()` call
2. **Selenium Required**: Make sure Selenium middleware is working
3. **Chrome Version**: Spider automatically detects and uses correct ChromeDriver
4. **Deduplication**: Plans with same name are automatically deduplicated

## 🐛 Troubleshooting

If CSV is not being written:

1. Check the log for:
   ```
   ✅ CSV file created and headers written
   ```

2. Verify output folder was created:
   ```bash
   ls -la etisalat_output/
   ```

3. Check for write errors in logs:
   ```
   ❌ Failed to write to CSV
   ```

4. Verify pipelines are not blocking items:
   - Pipelines should clean and validate, not drop items
   - Check for `🗑️  Dropping duplicate` messages

## 📈 Real-Time Monitoring

You can monitor the CSV file in real-time:

```bash
# Watch the CSV file grow
watch -n 1 'wc -l etisalat_output/etisalat_complete_*.csv'

# Tail the CSV file
tail -f etisalat_output/etisalat_complete_*.csv
```

## ✅ Success Indicators

- CSV file created immediately when spider starts
- Headers visible in CSV file right away
- New rows appear in CSV as each plan is scraped
- Log shows `💾 ✅ WRITTEN TO CSV` after each plan
- Final report shows total plans extracted

---

**Author**: Mohamed Atef Fahmi
**Date**: 2025-11-21
**Version**: 4.0 (Immediate CSV Writing)
