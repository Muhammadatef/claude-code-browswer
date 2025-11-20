# Etisalat vs du.ae - HTML Structure Comparison

## Side-by-Side Column Mapping

| Column Name | du.ae | Etisalat |
|-------------|-------|----------|
| **Name** | `h4.text-h6.white--text` | `ion-card-title.title` or `h4.text-h6.white--text` |
| **Description** | `.d-flex.flex-row.justify-center.align-center` | `.eand-badge__container .eand-badge` |
| **Price_Actual** | `.text-h5` | `.text-h5` or `.eand-tariff-card__price-wrapper` |
| **Price_Original** | `.text-decoration-line-through.text--h6` | `.text-decoration-line-through` |
| **Discount** | `.text-overline.white--lighten80.text-truncate` | `.text-overline.white--lighten80.text-truncate` or `.promotion-container` |
| **Main_Group** | `a.link` | `a.link` or URL-based |
| **Group** | `.v-tab.v-tab--active.is-active.mr-5.ms-5` | `.v-tab.v-tab--active` |
| **Benefit_1-5** | `.text-overline.text-truncate` | `.text-overline.text-truncate` or `.eand-tariff-card-body div` |
| **Speed** | (in benefits) | `.eand-tariff-card-body` with label "Speed" or pattern `\d+\s*Mbps` |
| **Minutes_Category** | Derived from content | Derived: "Flexi (International + Local)" or "Local Only" |
| **Commitment** | `.text-overline.white--lighten80.text-truncate.mb-1[title]` | `.contract-duration-container` or `[title*="contract"]` |
| **Product Codes** | `data-gtin`, `data-ean`, `data-uae-gtin` | `data-gtin`, `data-ean`, `data-uae-gtin` (rare) |

---

## Detailed Comparison Table

### Column: **Name**

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<h4>` | `text-h6 white--text` | `<h4 class="text-h6 white--text"><font dir="auto" style="vertical-align: inherit;">Power Plan 125</font></h4>` |
| **Etisalat** | `<ion-card-title>` or `<h4>` | `ion-card-title.title` or `text-h6 white--text` | `<ion-card-title class="title md hydrated"><font dir="auto">Power Plan 125</font></ion-card-title>` |

---

### Column: **Description**

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<div>` | `d-flex flex-row justify-center align-center` | `<div class="d-flex flex-row justify-center align-center"><span>calling</span></div>` |
| **Etisalat** | `<div>` with badges | `eand-badge__container`, `eand-badge` | `<div class="eand-badge__container"><div class="eand-badge"><font dir="auto">Calling</font></div></div>` |

---

### Column: **Price_Actual**

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<div>` | `text-h5` | `<div class="text-h5"><font dir="auto">AED 94</font></div>` |
| **Etisalat** | `<div>` | `text-h5` or `eand-tariff-card__price-wrapper` | `<div class="text-h5"><font dir="auto">AED 94</font><span class="text-caption">/month</span></div>` |

---

### Column: **Price_Original**

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<span>` | `text-decoration-line-through text--h6` | `<span class="text-decoration-line-through text--h6"><font dir="auto">AED 125</font></span>` |
| **Etisalat** | `<span>` | `text-decoration-line-through` | `<span class="text-decoration-line-through text--h6"><font dir="auto">AED 125</font></span>` |

---

### Column: **Discount**

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<div>` | `text-overline white--lighten80 text-truncate` | `<div class="text-overline white--lighten80 text-truncate"><font dir="auto">Save 25% for 3 months</font></div>` |
| **Etisalat** | `<div>` | `text-overline white--lighten80 text-truncate` or `promotion-container` | `<div class="text-overline white--lighten80 text-truncate"><font dir="auto">Save 25% for 3 months</font></div>` |

---

### Column: **Main_Group**

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<a>` | `link` | `<a class="link"><font dir="auto">Postpaid plans</font></a>` |
| **Etisalat** | `<a>` or URL-based | `link` | `<a href="/mobile/postpaid-plans" class="link"><font dir="auto">Postpaid plans</font></a>` |

**Note:** For Etisalat, often derived from URL:
- `/mobile/postpaid` → "Postpaid plans"
- `/mobile/prepaid` → "Prepaid plans"
- `/home/elife` → "Home Internet"

---

### Column: **Group** (Sub-category)

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<div>` (active tab) | `v-tab v-tab--active is-active mr-5 ms-5` | `<div class="v-tab v-tab--active is-active mr-5 ms-5"><font dir="auto">Power Plans</font></div>` |
| **Etisalat** | `<div>` (active tab) | `v-tab v-tab--active` | `<div class="v-tab v-tab--active" role="tab"><font dir="auto">Power Plans</font></div>` |

---

### Column: **Benefit_1** (e.g., 13 GB)

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<span>` | `text-overline text-truncate` | `<span class="text-overline text-truncate"><font dir="auto">13 GB</font></span>` |
| **Etisalat** | `<span>` or `<div>` | `text-overline text-truncate` or `.fs-14.fs-lg-16.fw-600` | `<div class="fs-14 fs-lg-16 fw-600"><font dir="auto">13 GB</font></div>` |

---

### Column: **Benefit_2** (e.g., Carry-over data)

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<span>` (multiple) | `text-overline text-truncate` | `<span class="text-overline text-truncate"><font dir="auto">Carry-over data</font></span><span class="text-overline text-truncate"><font dir="auto"> up to 6.5 GB</font></span>` |
| **Etisalat** | `<span>` or benefit row | `text-overline text-truncate` | Similar to du.ae |

---

### Column: **Benefit_3** (e.g., Roaming data)

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<span>` | `text-overline text-truncate` | `<span class="text-overline text-truncate"><font dir="auto">100 MB roaming data</font></span>` |
| **Etisalat** | `<span>` | `text-overline text-truncate` | Similar to du.ae |

---

### Column: **Benefit_4** (e.g., WiFi data)

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<span>` (multiple) | `text-overline text-truncate` | `<span class="text-overline text-truncate"><font dir="auto">26 GB</font></span><span class="text-overline text-truncate"><font dir="auto"> free data WiFi UAE</font></span>` |
| **Etisalat** | `<span>` | `text-overline text-truncate` | Similar to du.ae |

---

### Column: **Benefit_5** (e.g., Flexi minutes)

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<span>` (multiple) | `text-overline text-truncate` | `<span class="text-overline text-truncate"><font dir="auto">400</font></span><span class="text-overline text-truncate"><font dir="auto"> Flexi mins (nat'l & int'l)</font></span>` |
| **Etisalat** | `<span>` | `text-overline text-truncate` | Similar to du.ae |

---

### Column: **Speed** (Internet Speed)

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | (mixed with benefits) | `text-overline text-truncate` | Extracted via pattern matching |
| **Etisalat** | `<div>` in card body | `.eand-tariff-card-body` with label | `<div class="eand-tariff-card-body"><div class="label">Speed</div><div class="fs-14 fs-lg-16 fw-600"><font dir="auto">100 Mbps</font></div></div>` |

**Extraction:** Pattern matching `\d+\s*(?:Mbps|Gbps|MB/s|GB/s)`

---

### Column: **Minutes_Category** (NEW)

| Website | Determination | Values |
|---------|---------------|--------|
| **du.ae** | Content analysis | "Flexi (International + Local)" or "Local Only" |
| **Etisalat** | Content analysis | "Flexi (International + Local)" or "Local Only" |

**Logic:**
```python
if "flexi" in text.lower() or "international" in text.lower():
    return "Flexi (International + Local)"
else:
    return "Local Only"
```

---

### Column: **Local_Minutes**

| Website | Extraction Method |
|---------|-------------------|
| **du.ae** | Extract number from Benefit_5 text: `(\d+)\s*(?:flexi\s*)?min` |
| **Etisalat** | Extract number from minutes text: `(\d+)\s*(?:flexi\s*)?min` |

**Examples:**
- "400 Flexi mins" → **"400"**
- "500 local minutes" → **"500"**

---

### Column: **International_Minutes**

| Website | Determination |
|---------|---------------|
| **du.ae** | If Minutes_Category = "Flexi", use Local_Minutes value; else empty |
| **Etisalat** | If Minutes_Category = "Flexi", use Local_Minutes value; else empty |

---

### Column: **Commitment** (Contract Duration)

| Website | Element | Class/Attribute | outerHTML Example |
|---------|---------|-----------------|-------------------|
| **du.ae** | `<div>` | `text-overline white--lighten80 text-truncate mb-1` with `title` attribute | `<div class="text-overline white--lighten80 text-truncate mb-1" title="12-month contract"><font dir="auto">12-month contract</font></div>` |
| **Etisalat** | `<div>` | `contract-duration-container` or `[title*="contract"]` | `<div class="contract-duration-container"><span><font dir="auto">12-month contract</font></span></div>` |

---

### Columns: **GTIN_Code, UAE_GTIN, EAN_Code**

| Website | Element | Attributes | Notes |
|---------|---------|------------|-------|
| **du.ae** | Card or parent | `data-gtin`, `data-uae-gtin`, `data-ean` | Rarely visible on page |
| **Etisalat** | Card or parent | `data-gtin`, `data-uae-gtin`, `data-ean` | Rarely visible on page |

**Extraction:**
```python
gtin = card.get_attribute('data-gtin')
uae_gtin = card.get_attribute('data-uae-gtin')
ean = card.get_attribute('data-ean')
```

**Note:** These codes are often NOT present on either website's front-end. May need to:
- Check page meta tags
- Inspect JSON-LD structured data
- Check API responses
- Look at product detail pages

---

## Navigation Elements Comparison

### "More Details" Button

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<button>` | Various | `<button class="btn-details">More details</button>` |
| **Etisalat** | `<button>` | `.more-details-btn`, `.btn-details` | `<button class="btn more-details-btn" aria-label="More details"><font dir="auto">More details</font></button>` |

**Finding Strategy:**
- Search for button with text containing "more", "detail", or "view"
- Check `aria-label` attributes
- Try multiple selectors

---

### Swiper "Next" Button

| Website | Element | Class | outerHTML Example |
|---------|---------|-------|-------------------|
| **du.ae** | `<div>` | `swiper-button-next custom-swiper-button-next d-none d-lg-block` | `<div class="swiper-button-next custom-swiper-button-next d-none d-lg-block" tabindex="0" role="button" aria-label="Next slide" aria-controls="swiper-wrapper-72f4a7286f34fbbe" aria-disabled="false"></div>` |
| **Etisalat** | `<div>` | `swiper-button-next` (simpler) | `<div class="swiper-button-next" aria-label="Next slide" aria-disabled="false"></div>` |

**Important:** Check `aria-disabled` attribute:
- `aria-disabled="false"` → More slides available
- `aria-disabled="true"` → No more slides

---

## Key Similarities

Both du.ae and Etisalat use:

1. **Vuetify Framework** → Similar CSS class naming (`.v-tab`, `.text-h5`, etc.)
2. **Font elements** → Text wrapped in `<font dir="auto">` for RTL support
3. **Swiper.js** → Carousel navigation with `.swiper-button-next`
4. **Similar structure** → Benefits as `.text-overline.text-truncate` spans
5. **Similar pricing** → `.text-h5` for actual price, `.text-decoration-line-through` for original

---

## Key Differences

| Aspect | du.ae | Etisalat |
|--------|-------|----------|
| **Card element** | Standard `<div>` or `<article>` | Ionic `<ion-card>` |
| **Title element** | `<h4>` | `<ion-card-title>` |
| **Price container** | Generic div | `.eand-tariff-card__price-wrapper` |
| **Description** | Single div | Badge container with multiple badges |
| **Speed location** | Mixed with benefits | Separate field in card body with label |
| **Commitment** | `title` attribute important | Dedicated container `.contract-duration-container` |

---

## Spider Implementation: Unified Approach

Since both websites are similar, you can use a unified extraction approach:

```python
def extract_field(card, selectors_list):
    """Try multiple selectors until one succeeds"""
    for selector in selectors_list:
        try:
            elem = card.find_element(By.CSS_SELECTOR, selector)
            if elem.is_displayed():
                text = elem.text.strip()
                if text:
                    return text
        except:
            continue
    return None

# Example: Extract name from both sites
name = extract_field(card, [
    'ion-card-title.title',     # Etisalat
    'h4.text-h6.white--text',   # Both
    '.plan-name',               # Generic fallback
])
```

---

## Testing Checklist

### du.ae
- [ ] https://shop.du.ae/en/personal/postpaid/emirati-plans
- [ ] https://shop.du.ae/en/personal/s-du-postpaid-plans
- [ ] https://shop.du.ae/en/personal/s-du-prepaid-flexi-plans

### Etisalat
- [ ] https://www.etisalat.ae/en/c/mobile/postpaid-plans.html
- [ ] https://www.etisalat.ae/en/c/mobile/prepaid-plans.html
- [ ] https://www.etisalat.ae/en/c/home/internet-plans.html

---

## Summary: Quick Reference

### Name
- **du.ae:** `h4.text-h6.white--text`
- **Etisalat:** `ion-card-title.title`

### Price
- **Both:** `.text-h5` (actual), `.text-decoration-line-through` (original)

### Benefits
- **Both:** `.text-overline.text-truncate` (extract first 5)

### Speed
- **Both:** Pattern match `\d+\s*Mbps` in text content

### Minutes Category
- **Both:** Derived from content ("flexi"/"international" → Flexi; else → Local Only)

### Navigation
- **Both:** `.swiper-button-next` (check `aria-disabled`)

---

**Created:** 2025-11-20
**For:** Unified spider supporting both du.ae and Etisalat UAE
