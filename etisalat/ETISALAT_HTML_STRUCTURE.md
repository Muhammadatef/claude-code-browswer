# Etisalat UAE - HTML Structure & CSS Classes Reference

## Plan Card Container

**Element:** `<ion-card>` or `<div>` with class `eand-tariff-card`

```html
<ion-card class="eand-tariff-card md hydrated">
  <!-- Plan content here -->
</ion-card>
```

---

## Data Fields Extraction Guide

### 1. **Name** (Plan Name)

| Property | Value |
|----------|-------|
| **Element** | `<ion-card-title>` or `<h4>` |
| **CSS Class** | `ion-card-title.title` or `h4.text-h6.white--text` |
| **Selectors** | `ion-card-title.title`, `.plan-name`, `h4.text-h6.white--text` |
| **Parent Container** | `.eand-tariff-card__header` |

**Example outerHTML:**
```html
<ion-card-title class="title md hydrated">
  <font dir="auto" style="vertical-align: inherit;">Power Plan 125</font>
</ion-card-title>
```

Or:

```html
<h4 class="text-h6 white--text">
  <font dir="auto" style="vertical-align: inherit;">Freedom Plan 150</font>
</h4>
```

---

### 2. **Description** (Plan Category/Type)

| Property | Value |
|----------|-------|
| **Element** | `<div>` with badges or `<span>` |
| **CSS Class** | `.eand-badge__container`, `.eand-badge`, `.d-flex.flex-row.justify-center.align-center` |
| **Selectors** | `.eand-badge__container .eand-badge`, `.plan-description` |

**Example outerHTML:**
```html
<div class="eand-badge__container">
  <div class="eand-badge">
    <font dir="auto" style="vertical-align: inherit;">Calling</font>
  </div>
  <div class="eand-badge">
    <font dir="auto" style="vertical-align: inherit;">Data</font>
  </div>
</div>
```

Or:

```html
<div class="d-flex flex-row justify-center align-center">
  <span class="text-caption">
    <font dir="auto" style="vertical-align: inherit;">calling</font>
  </span>
</div>
```

---

### 3. **Price_Actual** (Current Price)

| Property | Value |
|----------|-------|
| **Element** | `<div>` or `<span>` |
| **CSS Class** | `.text-h5`, `.eand-tariff-card__price-wrapper`, `.price-actual` |
| **Parent** | `.eand-tariff-card__price-wrapper` |

**Example outerHTML:**
```html
<div class="eand-tariff-card__price-wrapper">
  <div class="text-h5">
    <font dir="auto" style="vertical-align: inherit;">AED 94</font>
    <span class="text-caption">
      <font dir="auto" style="vertical-align: inherit;">/month</font>
    </span>
  </div>
</div>
```

Or:

```html
<span class="text-h5 font-weight-bold">
  <font dir="auto" style="vertical-align: inherit;">AED 125</font>
</span>
```

---

### 4. **Price_Original** (Original Price Before Discount)

| Property | Value |
|----------|-------|
| **Element** | `<span>` |
| **CSS Class** | `.text-decoration-line-through`, `.text--h6`, `.price-original` |
| **Distinctive Feature** | Has `text-decoration-line-through` style |

**Example outerHTML:**
```html
<span class="text-decoration-line-through text--h6">
  <font dir="auto" style="vertical-align: inherit;">AED 125</font>
</span>
```

Or:

```html
<span class="original-price text-decoration-line-through grey--text">
  <font dir="auto" style="vertical-align: inherit;">AED 150</font>
</span>
```

---

### 5. **Discount** (Discount/Promotion Text)

| Property | Value |
|----------|-------|
| **Element** | `<div>` or `<span>` |
| **CSS Class** | `.text-overline.white--lighten80.text-truncate`, `.promotion-container` |
| **Common Text** | Contains "Save", "%", "months", "Promotion" |

**Example outerHTML:**
```html
<div class="text-overline white--lighten80 text-truncate">
  <font dir="auto" style="vertical-align: inherit;">Save 25% for 3 months</font>
</div>
```

Or:

```html
<div class="promotion-container">
  <div class="promotion-text">
    <font dir="auto" style="vertical-align: inherit;">Limited time: 20% off</font>
  </div>
</div>
```

---

### 6. **Main_Group** (Top-level Category)

| Property | Value |
|----------|-------|
| **Element** | `<a>` link or breadcrumb |
| **CSS Class** | `.link`, `.breadcrumb-item` |
| **Location** | Top navigation or breadcrumb |
| **Extraction** | Also derive from URL (postpaid → "Postpaid plans") |

**Example outerHTML:**
```html
<a href="/mobile/postpaid-plans" class="link">
  <font dir="auto" style="vertical-align: inherit;">Postpaid plans</font>
</a>
```

**Common Values:**
- "Postpaid plans"
- "Prepaid plans"
- "Mobile Plans"
- "Home Internet"

---

### 7. **Group** (Sub-category/Tab)

| Property | Value |
|----------|-------|
| **Element** | `<div>` or `<button>` (active tab) |
| **CSS Class** | `.v-tab.v-tab--active`, `.is-active`, `.mr-5.ms-5` |
| **Location** | Tab navigation within plan page |

**Example outerHTML:**
```html
<div class="v-tab v-tab--active is-active mr-5 ms-5" role="tab">
  <font dir="auto" style="vertical-align: inherit;">Power Plans</font>
</div>
```

**Common Values:**
- "Power Plans"
- "Freedom Plans"
- "Smart Plans"
- "Wasel Flexi"
- "Control Line"

---

### 8. **Benefit_1** (First Benefit - Usually Data)

| Property | Value |
|----------|-------|
| **Element** | `<span>` or `<div>` |
| **CSS Class** | `.text-overline.text-truncate` |
| **Parent** | `.eand-tariff-card-body` |
| **Common Content** | Data amounts (GB, MB) |

**Example outerHTML:**
```html
<span class="text-overline text-truncate">
  <font dir="auto" style="vertical-align: inherit;">13 GB</font>
</span>
```

Or:

```html
<div class="benefit-item">
  <div class="benefit-label">Local Data</div>
  <div class="benefit-value fs-14 fs-lg-16 fw-600">
    <font dir="auto" style="vertical-align: inherit;">20 GB</font>
  </div>
</div>
```

---

### 9. **Benefit_2** (Second Benefit - Carry-over Data)

| Property | Value |
|----------|-------|
| **Element** | `<span>` |
| **CSS Class** | `.text-overline.text-truncate` |
| **Common Content** | "Carry-over data", "Rollover" |

**Example outerHTML:**
```html
<span class="text-overline text-truncate">
  <font dir="auto" style="vertical-align: inherit;">Carry-over data</font>
</span>
<span class="text-overline text-truncate">
  <font dir="auto" style="vertical-align: inherit;"> up to 6.5 GB</font>
</span>
```

---

### 10. **Benefit_3** (Third Benefit - Roaming Data)

| Property | Value |
|----------|-------|
| **Element** | `<span>` |
| **CSS Class** | `.text-overline.text-truncate` |
| **Common Content** | "roaming data", "MB roaming" |

**Example outerHTML:**
```html
<span class="text-overline text-truncate">
  <font dir="auto" style="vertical-align: inherit;">100 MB roaming data</font>
</span>
```

---

### 11. **Benefit_4** (Fourth Benefit - WiFi Data)

| Property | Value |
|----------|-------|
| **Element** | `<span>` |
| **CSS Class** | `.text-overline.text-truncate` |
| **Common Content** | "WiFi UAE", "free data" |

**Example outerHTML:**
```html
<span class="text-overline text-truncate">
  <font dir="auto" style="vertical-align: inherit;">26 GB</font>
</span>
<span class="text-overline text-truncate">
  <font dir="auto" style="vertical-align: inherit;"> free data WiFi UAE</font>
</span>
```

---

### 12. **Benefit_5** (Fifth Benefit - Minutes)

| Property | Value |
|----------|-------|
| **Element** | `<span>` |
| **CSS Class** | `.text-overline.text-truncate` |
| **Common Content** | "Flexi mins", "local minutes", "international" |

**Example outerHTML:**
```html
<span class="text-overline text-truncate">
  <font dir="auto" style="vertical-align: inherit;">400</font>
</span>
<span class="text-overline text-truncate">
  <font dir="auto" style="vertical-align: inherit;"> Flexi mins (nat'l & int'l)</font>
</span>
```

---

### 13. **Speed** (Internet Speed)

| Property | Value |
|----------|-------|
| **Element** | `<div>` or `<span>` |
| **CSS Class** | `.eand-tariff-card-body div`, `[class*="speed"]`, `.fs-14.fs-lg-16.fw-600` |
| **Label** | Usually has "Speed" or "Internet speed" label |
| **Common Values** | "100 Mbps", "500 Mbps", "1 Gbps" |

**Example outerHTML:**
```html
<div class="eand-tariff-card-body">
  <div class="label-text">
    <font dir="auto" style="vertical-align: inherit;">Speed</font>
  </div>
  <div class="fs-14 fs-lg-16 fw-600">
    <font dir="auto" style="vertical-align: inherit;">100 Mbps</font>
  </div>
</div>
```

**Pattern matching:** `\d+\s*(?:Mbps|Gbps|MB/s|GB/s)`

---

### 14. **Minutes_Category** (Type of Minutes)

| Property | Value |
|----------|-------|
| **Determination** | Based on content analysis |
| **If contains:** "Flexi" OR "international" → **"Flexi (International + Local)"** |
| **Otherwise:** → **"Local Only"** |
| **Source Elements** | Same as Benefit_5, analyze text content |

**Logic:**
```python
if "flexi" in text.lower() or "international" in text.lower():
    category = "Flexi (International + Local)"
else:
    category = "Local Only"
```

**Example texts:**
- "400 Flexi mins (nat'l & int'l)" → **Flexi (International + Local)**
- "500 local minutes" → **Local Only**

---

### 15. **Local_Minutes** (Local Calling Minutes)

| Property | Value |
|----------|-------|
| **Element** | `<span>` within benefits |
| **CSS Class** | `.text-overline.text-truncate` |
| **Pattern** | Extract number from minutes text |

**Extraction pattern:** `(\d+)\s*(?:flexi\s*)?min`

**Example:**
- Text: "400 Flexi mins" → Extract: **"400"**
- Text: "500 local minutes" → Extract: **"500"**

---

### 16. **International_Minutes** (International Calling Minutes)

| Property | Value |
|----------|-------|
| **Determination** | If Minutes_Category = "Flexi", use same as Local_Minutes |
| **Otherwise** | Empty or null |

**Logic:**
```python
if minutes_category == "Flexi (International + Local)":
    international_minutes = local_minutes
else:
    international_minutes = None
```

---

### 17. **Commitment** (Contract Duration)

| Property | Value |
|----------|-------|
| **Element** | `<div>` or `<span>` |
| **CSS Class** | `.text-overline.white--lighten80.text-truncate.mb-1`, `.contract-duration-container` |
| **Attribute** | `title` attribute often contains contract info |
| **Common Values** | "12-month contract", "24-month contract", "No commitment" |

**Example outerHTML:**
```html
<div class="text-overline white--lighten80 text-truncate mb-1"
     title="12-month contract">
  <font dir="auto" style="vertical-align: inherit;">12-month contract</font>
</div>
```

Or:

```html
<div class="contract-duration-container">
  <span class="contract-text">
    <font dir="auto" style="vertical-align: inherit;">No commitment</font>
  </span>
</div>
```

---

### 18. **GTIN_Code** (Product GTIN)

| Property | Value |
|----------|-------|
| **Element** | Product metadata (usually not visible) |
| **Attribute** | `data-gtin`, `data-product-code` |
| **Location** | On plan card or parent container |

**Example outerHTML:**
```html
<ion-card class="eand-tariff-card"
          data-gtin="1234567890123"
          data-product-id="prod-power-125">
  <!-- Plan content -->
</ion-card>
```

**Note:** GTIN codes are often not displayed on Etisalat pages. Check:
- `data-gtin` attribute
- `data-product-code` attribute
- Meta tags in page head
- Structured data (JSON-LD)

---

### 19. **UAE_GTIN** (UAE-specific GTIN)

| Property | Value |
|----------|-------|
| **Element** | Product metadata |
| **Attribute** | `data-uae-gtin`, `data-local-code` |
| **Location** | Same as GTIN_Code |

**Example outerHTML:**
```html
<ion-card data-uae-gtin="AE1234567890">
  <!-- Plan content -->
</ion-card>
```

**Note:** Rarely available on Etisalat pages.

---

### 20. **EAN_Code** (European Article Number)

| Property | Value |
|----------|-------|
| **Element** | Product metadata |
| **Attribute** | `data-ean`, `data-ean-code` |
| **Location** | Same as GTIN_Code |

**Example outerHTML:**
```html
<ion-card data-ean="1234567890128">
  <!-- Plan content -->
</ion-card>
```

**Note:** Rarely available on Etisalat pages.

---

## Navigation Elements

### "More Details" Button

| Property | Value |
|----------|-------|
| **Element** | `<button>` or `<a>` |
| **CSS Class** | `.btn-details`, `.more-details-btn`, `.view-details` |
| **Common Text** | "More details", "View details", "Learn more" |
| **aria-label** | "More details", "View plan details" |

**Example outerHTML:**
```html
<button class="btn btn-primary more-details-btn"
        aria-label="More details">
  <font dir="auto" style="vertical-align: inherit;">More details</font>
</button>
```

Or:

```html
<a href="#plan-details" class="view-details link">
  <font dir="auto" style="vertical-align: inherit;">View details</font>
</a>
```

---

### Swiper "Next" Button

| Property | Value |
|----------|-------|
| **Element** | `<div>` or `<button>` |
| **CSS Class** | `.swiper-button-next.custom-swiper-button-next.d-none.d-lg-block` |
| **aria-label** | "Next slide" |
| **Attributes** | `aria-disabled="false"` (when enabled) |

**Example outerHTML:**
```html
<div class="swiper-button-next custom-swiper-button-next d-none d-lg-block"
     tabindex="0"
     role="button"
     aria-label="Next slide"
     aria-controls="swiper-wrapper-72f4a7286f34fbbe"
     aria-disabled="false">
</div>
```

**Usage Notes:**
- Check `aria-disabled` attribute before clicking
- `aria-disabled="true"` means no more slides
- `aria-disabled="false"` means more slides available

---

## Complete Extraction Workflow

### Step 1: Navigate to Page
```python
driver.get("https://www.etisalat.ae/en/c/mobile/postpaid-plans.html")
time.sleep(3)
```

### Step 2: Find Plan Cards
```python
cards = driver.find_elements(By.CSS_SELECTOR, "ion-card.eand-tariff-card")
```

### Step 3: For Each Card:

1. **Scroll into view**
   ```python
   driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
   time.sleep(1)
   ```

2. **Click "More Details" (if exists)**
   ```python
   more_btn = card.find_element(By.CSS_SELECTOR, "button.more-details-btn")
   more_btn.click()
   time.sleep(2)
   ```

3. **Extract all data fields** using selectors above

4. **Close modal** (if opened)
   ```python
   close_btn = driver.find_element(By.CSS_SELECTOR, ".modal-close")
   close_btn.click()
   ```

### Step 4: Navigate to Next Slide
```python
next_btn = driver.find_element(By.CSS_SELECTOR, ".swiper-button-next")
if next_btn.get_attribute("aria-disabled") != "true":
    next_btn.click()
    time.sleep(2)
    # Repeat from Step 2
```

---

## CSS Selector Priority Guide

For each field, try selectors in this order:

### Name:
1. `ion-card-title.title`
2. `h4.text-h6.white--text`
3. `.plan-name`
4. `h3`, `h4`, `h5`

### Price_Actual:
1. `.text-h5`
2. `.eand-tariff-card__price-wrapper .text-h5`
3. `.price-actual`
4. `[class*="price"]`

### Benefits:
1. `.text-overline.text-truncate`
2. `.eand-tariff-card-body div.fs-14`
3. `.benefit-item`
4. `ul li`

---

## Common Issues & Solutions

### Issue 1: Font elements
**Problem:** Text wrapped in `<font dir="auto">` elements

**Solution:** Use `.text` or `.text_content()` to get all text, ignoring child elements

### Issue 2: Multiple matches
**Problem:** Selector returns multiple elements

**Solution:**
- Use parent containers to narrow scope
- Filter by `is_displayed()`
- Check text content length

### Issue 3: Dynamic content
**Problem:** Elements load after page load

**Solution:**
- Wait for specific elements: `WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))`
- Add delays: `time.sleep(2)`

---

## Spider Implementation Checklist

✅ **Navigation**
- [ ] Load page and wait for cards
- [ ] Find all plan cards on current view
- [ ] Click "More Details" for each card
- [ ] Close modals after extraction
- [ ] Click swiper "Next" button
- [ ] Check `aria-disabled` before clicking next
- [ ] Loop until no more slides

✅ **Extraction (per card)**
- [ ] Name (required)
- [ ] Description
- [ ] Price_Actual (required)
- [ ] Price_Original
- [ ] Discount
- [ ] Main_Group (from URL)
- [ ] Group (from active tab)
- [ ] Benefits 1-5
- [ ] Speed (with pattern matching)
- [ ] Minutes_Category (derived)
- [ ] Local_Minutes (extracted)
- [ ] International_Minutes (derived)
- [ ] Commitment
- [ ] Product codes (if available)

✅ **Validation**
- [ ] Check required fields (Name, Price_Actual) not empty
- [ ] Validate price format
- [ ] Ensure at least one benefit extracted
- [ ] Log warnings for missing data

---

## Example: Complete Card HTML Structure

```html
<ion-card class="eand-tariff-card md hydrated">
  <!-- Header -->
  <div class="eand-tariff-card__header">
    <ion-card-title class="title md hydrated">
      <font dir="auto">Power Plan 125</font>
    </ion-card-title>

    <div class="eand-badge__container">
      <div class="eand-badge">
        <font dir="auto">Calling</font>
      </div>
    </div>
  </div>

  <!-- Body -->
  <div class="eand-tariff-card-body">
    <div class="benefit-row">
      <div class="label">Local Data</div>
      <div class="value fs-14 fs-lg-16 fw-600">
        <font dir="auto">13 GB</font>
      </div>
    </div>

    <div class="benefit-row">
      <div class="label">Speed</div>
      <div class="value fs-14 fs-lg-16 fw-600">
        <font dir="auto">100 Mbps</font>
      </div>
    </div>

    <span class="text-overline text-truncate">
      <font dir="auto">400 Flexi mins (nat'l & int'l)</font>
    </span>
  </div>

  <!-- Footer -->
  <div class="eand-tariff-card__price-wrapper">
    <div class="text-h5">
      <font dir="auto">AED 94</font>
      <span class="text-caption">
        <font dir="auto">/month</font>
      </span>
    </div>
    <span class="text-decoration-line-through text--h6">
      <font dir="auto">AED 125</font>
    </span>
  </div>

  <div class="promotion-container">
    <div class="text-overline white--lighten80 text-truncate">
      <font dir="auto">Save 25% for 3 months</font>
    </div>
  </div>

  <div class="contract-duration-container">
    <div class="text-overline white--lighten80 text-truncate mb-1"
         title="12-month contract">
      <font dir="auto">12-month contract</font>
    </div>
  </div>

  <!-- Actions -->
  <button class="btn more-details-btn" aria-label="More details">
    <font dir="auto">More details</font>
  </button>
</ion-card>
```

---

## Metadata Fields

Add these to every extracted item:

```python
item['url'] = driver.current_url
item['scrape_ts'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
item['domain'] = "etisalat.ae"
item['insert_ts'] = ""  # For database insertion
item['frequency'] = "daily"
```

---

## Testing Checklist

- [ ] Test on postpaid plans page
- [ ] Test on prepaid plans page
- [ ] Test on home internet page
- [ ] Verify "More Details" click works
- [ ] Verify swiper navigation works
- [ ] Verify all fields extracted
- [ ] Verify minutes categorization logic
- [ ] Verify speed extraction with pattern matching
- [ ] Check CSV output format
- [ ] Validate data completeness

---

**Last Updated:** 2025-11-20
**Spider Version:** 1.0
**Framework:** Etisalat uses Vue.js/Vuetify and Ionic components
