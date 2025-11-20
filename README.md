# du Mobile Plans Scraper

This Apify Actor scrapes postpaid and prepaid mobile plans from the du.ae website, extracting detailed information about each plan including pricing, benefits, and commitments.

## Features

- Scrapes both postpaid and prepaid mobile plans from du.ae
- Extracts comprehensive plan details including:
  - Plan name and description
  - Current and original prices
  - Discounts and promotional offers
  - Plan categories (Main Group and Group)
  - Up to 5 benefits per plan
  - Contract commitment details
  - Product codes (GTIN, UAE_GTIN, EAN if available)

## Input Configuration

The Actor accepts the following input parameters:

### start_urls (array)
List of URLs to scrape. By default, it scrapes:
- https://shop.du.ae/en/personal/postpaid/emirati-plans
- https://shop.du.ae/en/personal/s-du-postpaid-plans
- https://shop.du.ae/en/personal/s-du-metallic-plans?showLoader=true
- https://shop.du.ae/en/personal/s-du-prepaid-flexi-plans
- https://shop.du.ae/en/personal/s-du-prepaid-easy-plans

You can customize these URLs or add additional ones.

### headless (boolean)
Run the browser in headless mode. Default is `true`. Set to `false` for debugging purposes.

Example input:
```json
{
  "start_urls": [
    {
      "url": "https://shop.du.ae/en/personal/postpaid/emirati-plans"
    },
    {
      "url": "https://shop.du.ae/en/personal/s-du-postpaid-plans"
    },
    {
      "url": "https://shop.du.ae/en/personal/s-du-metallic-plans?showLoader=true"
    },
    {
      "url": "https://shop.du.ae/en/personal/s-du-prepaid-flexi-plans"
    },
    {
      "url": "https://shop.du.ae/en/personal/s-du-prepaid-easy-plans"
    }
  ],
  "headless": true
}
```

## Output Schema

The Actor outputs data in the following format:

| Field | Type | Description |
|-------|------|-------------|
| Name | string | Plan name (e.g., "Power Plan 125") |
| Description | string | Brief description of the plan (e.g., "calling") |
| Price_Actual | string | Current price (e.g., "AED 94") |
| Price_Original | string | Original price before discount (e.g., "AED 125") |
| Discount | string | Discount information (e.g., "Save 25% for 3 months") |
| Main_Group | string | Main category (e.g., "Postpaid plans" or "Prepaid plans") |
| Group | string | Plan group/category (e.g., "Power Plans", "Smart Plans") |
| Benefit_1 | string | First benefit (e.g., "13 GB") |
| Benefit_2 | string | Second benefit (e.g., "Carry-over data up to 6.5 GB") |
| Benefit_3 | string | Third benefit (e.g., "100 MB roaming data") |
| Benefit_4 | string | Fourth benefit (e.g., "26 GB free data WiFi UAE") |
| Benefit_5 | string | Fifth benefit (e.g., "400 Flexi mins (nat'l & int'l)") |
| Commitment | string | Contract commitment (e.g., "12-month contract") |
| GTIN_Code | string | Global Trade Item Number (if available) |
| UAE_GTIN | string | UAE-specific GTIN (if available) |
| EAN_Code | string | European Article Number (if available) |
| Source_URL | string | URL where the plan was scraped from |

Example output:
```json
{
  "Name": "Power Plan 125",
  "Description": "calling",
  "Price_Actual": "AED 94",
  "Price_Original": "AED 125",
  "Discount": "Save 25% for 3 months",
  "Main_Group": "Postpaid plans",
  "Group": "Power Plans",
  "Benefit_1": "13 GB",
  "Benefit_2": "Carry-over data up to 6.5 GB",
  "Benefit_3": "100 MB roaming data",
  "Benefit_4": "26 GB free data WiFi UAE",
  "Benefit_5": "400 Flexi mins (nat'l & int'l)",
  "Commitment": "12-month contract",
  "GTIN_Code": null,
  "UAE_GTIN": null,
  "EAN_Code": null,
  "Source_URL": "https://shop.du.ae/en/personal/s-du-postpaid-plans"
}
```

## How It Works

1. The Actor navigates to the specified du.ae mobile plan pages
2. It waits for the page to fully load, including dynamic content
3. It identifies all plan cards on the page
4. For each plan card, it extracts all the relevant information using specific CSS selectors
5. It attempts to click through different tabs to capture all available plans
6. All extracted data is stored in the Apify dataset

## Technical Details

- Built using Apify SDK and Crawlee with Playwright
- Uses Chromium browser for rendering JavaScript-heavy pages
- Implements wait strategies to ensure dynamic content is loaded
- Handles multiple plan categories and tabs dynamically

## Local Development

To run this Actor locally:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

2. Run the Actor:
   ```bash
   python -m src.main
   ```

## Deployment

This Actor can be deployed to the Apify platform:

1. Push the code to your Apify account
2. The Actor will automatically build using the provided Dockerfile
3. Run the Actor from the Apify Console with your desired input configuration

## Notes

- The Actor is designed to work with the current du.ae website structure (as of November 2024)
- Website changes may require updates to the CSS selectors
- Product codes (GTIN, UAE_GTIN, EAN) may not always be available on the website
- The Actor respects the website's terms of service and implements appropriate delays

## Support

For issues or questions, please contact the Actor maintainer or refer to the Apify documentation at https://docs.apify.com
