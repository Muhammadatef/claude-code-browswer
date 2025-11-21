# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import re
from datetime import datetime
from itemadapter import ItemAdapter


class EandCleaningPipeline:
    """
    Pipeline for cleaning and transforming scraped Etisalat plan data.

    Handles:
    - Price normalization (extract numeric values)
    - Data value standardization (GB/MB normalization)
    - Minutes value cleaning (extract numbers, handle "Unlimited")
    - Speed value normalization (Mbps/Gbps)
    - WiFi hours extraction
    - Text field cleaning (strip whitespace, remove extra characters)
    - Null/None value handling
    """

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # 1. Clean Name
        adapter['Name'] = self.clean_text(adapter.get('Name'))

        # 2. Clean Description
        adapter['Description'] = self.clean_text(adapter.get('Description'))

        # 3. Clean and normalize Pricing fields
        adapter['Price_Actual'] = self.clean_price(adapter.get('Price_Actual'))
        adapter['Price_Original'] = self.clean_price(adapter.get('Price_Original'))
        adapter['Discount'] = self.clean_text(adapter.get('Discount'))

        # 4. Clean Category fields
        adapter['Main_Group'] = self.clean_text(adapter.get('Main_Group'))
        adapter['Group'] = self.clean_text(adapter.get('Group'))
        adapter['Navigational_Aid'] = self.clean_text(adapter.get('Navigational_Aid'))

        # 5. Clean and normalize Speed
        adapter['Speed'] = self.clean_speed(adapter.get('Speed'))

        # 6. Clean and normalize Data fields
        adapter['Local_Data'] = self.clean_data(adapter.get('Local_Data'))
        adapter['Roaming_Data'] = self.clean_data(adapter.get('Roaming_Data'))
        adapter['Entertainment_Packs_Data'] = self.clean_data(adapter.get('Entertainment_Packs_Data'))

        # 7. Clean Minutes fields (renamed from Local_Minutes)
        adapter['Minutes'] = self.clean_minutes(adapter.get('Minutes'))
        adapter['Minutes_Category'] = self.clean_text(adapter.get('Minutes_Category'))

        # 7b. Clean Variable fields
        adapter['Variable'] = self.clean_text(adapter.get('Variable'))
        adapter['Variable_value'] = self.clean_text(adapter.get('Variable_value'))

        # 8. Clean Entertainment Pack
        adapter['Entertainment_Pack'] = self.clean_entertainment_pack(adapter.get('Entertainment_Pack'))

        # 9. Clean WiFi Hours
        adapter['UAE_WiFi_Hours'] = self.clean_wifi_hours(adapter.get('UAE_WiFi_Hours'))

        # 10. Clean Additional Benefits
        adapter['Additional_Benefits'] = self.clean_text(adapter.get('Additional_Benefits'))

        # 11. Clean Promotion
        adapter['Promotion'] = self.clean_text(adapter.get('Promotion'))

        # 12. Clean Commitment
        adapter['Commitment'] = self.clean_commitment(adapter.get('Commitment'))

        # 13. Clean Product Codes
        adapter['GTIN_Code'] = self.clean_text(adapter.get('GTIN_Code'))
        adapter['UAE_GTIN'] = self.clean_text(adapter.get('UAE_GTIN'))
        adapter['EAN_Code'] = self.clean_text(adapter.get('EAN_Code'))

        # 14. Ensure metadata fields are present
        if not adapter.get('insert_ts'):
            adapter['insert_ts'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return item

    # ============================================================================
    # CLEANING METHODS
    # ============================================================================

    def clean_text(self, text):
        """Clean general text fields - remove extra whitespace, newlines"""
        if text is None or text == "N/A" or text == "":
            return None

        text = str(text).strip()

        # Remove excessive whitespace and newlines
        text = re.sub(r'\s+', ' ', text)

        # Remove leading/trailing special characters
        text = text.strip('.,;:!? \t\n\r')

        return text if text else None

    def clean_price(self, price):
        """
        Extract numeric price value from price string.

        Examples:
        - "AED 225/month" -> "225"
        - "225" -> "225"
        - "AED 225" -> "225"
        - "0" or "AED 0" -> "Pay as you go" (for prepaid plans)
        - None -> None
        """
        if not price:
            return None

        price = str(price).strip()

        # Extract numeric value (including decimals and commas)
        match = re.search(r'(\d+(?:,\d+)?(?:\.\d+)?)', price)
        if match:
            # Remove commas from number
            numeric_value = match.group(1).replace(',', '')

            # Handle AED 0 for prepaid plans -> "Pay as you go, Recharge on need"
            if numeric_value == '0':
                return "Pay as you go"

            return numeric_value

        return None

    def clean_speed(self, speed):
        """
        Normalize internet speed values.

        Examples:
        - "250 Mbps" -> "250 Mbps"
        - "1 Gbps" -> "1000 Mbps" (convert to Mbps)
        - "250Mbps" -> "250 Mbps" (add space)
        - "250" -> "250 Mbps" (assume Mbps)
        - None -> None
        """
        if not speed:
            return None

        speed = str(speed).strip()

        # Extract number and unit
        match = re.search(r'(\d+(?:\.\d+)?)\s*(Mbps|Gbps|mbps|gbps)?', speed, re.IGNORECASE)
        if not match:
            return None

        value = float(match.group(1))
        unit = match.group(2).lower() if match.group(2) else 'mbps'

        # Convert Gbps to Mbps
        if 'gbps' in unit:
            value = value * 1000
            unit = 'Mbps'
        else:
            unit = 'Mbps'

        # Format: "250 Mbps"
        if value.is_integer():
            return f"{int(value)} {unit}"
        else:
            return f"{value} {unit}"

    def clean_data(self, data):
        """
        Normalize data values (GB/MB).

        Examples:
        - "10GB" -> "10 GB"
        - "10 GB" -> "10 GB"
        - "1024 MB" -> "1 GB" (convert MB to GB if >= 1024)
        - "500 MB" -> "500 MB"
        - "Unlimited" -> "Unlimited"
        - None -> None
        """
        if not data:
            return None

        data = str(data).strip()

        # Handle "Unlimited" case
        if 'unlimited' in data.lower():
            return "Unlimited"

        # Extract number and unit
        match = re.search(r'(\d+(?:\.\d+)?)\s*(GB|MB|gb|mb)', data, re.IGNORECASE)
        if not match:
            return None

        value = float(match.group(1))
        unit = match.group(2).upper()

        # Convert MB to GB if >= 1024
        if unit == 'MB' and value >= 1024:
            value = value / 1024
            unit = 'GB'

        # Format: "10 GB" or "500 MB"
        if value.is_integer():
            return f"{int(value)} {unit}"
        else:
            return f"{value:.1f} {unit}"

    def clean_minutes(self, minutes):
        """
        Clean minutes values - extract numeric value or keep "Unlimited".

        Examples:
        - "800" -> "800"
        - "800 minutes" -> "800"
        - "Unlimited" -> "Unlimited"
        - "Unlimited local minutes" -> "Unlimited"
        - None -> None
        """
        if not minutes:
            return None

        minutes = str(minutes).strip()

        # Handle "Unlimited" case
        if 'unlimited' in minutes.lower():
            return "Unlimited"

        # Extract numeric value
        match = re.search(r'(\d+)', minutes)
        if match:
            return match.group(1)

        return None

    def clean_entertainment_pack(self, pack):
        """
        Clean entertainment pack values.

        Examples:
        - "1 FREE" -> "1 FREE"
        - "2 Free" -> "2 FREE"
        - "1" -> "1 FREE"
        - None -> None
        """
        if not pack:
            return None

        pack = str(pack).strip()

        # Standardize "FREE" capitalization
        pack = re.sub(r'\bfree\b', 'FREE', pack, flags=re.IGNORECASE)

        # If it's just a number, add "FREE"
        if pack.isdigit():
            return f"{pack} FREE"

        return pack

    def clean_wifi_hours(self, hours):
        """
        Clean WiFi hours - extract numeric value.

        Examples:
        - "100" -> "100"
        - "100 hours" -> "100"
        - "100 UAE Wi-Fi hours" -> "100"
        - None -> None
        """
        if not hours:
            return None

        hours = str(hours).strip()

        # Extract numeric value
        match = re.search(r'(\d+)', hours)
        if match:
            return match.group(1)

        return None

    def clean_commitment(self, commitment):
        """
        Normalize commitment values.

        Examples:
        - "12-month contract" -> "12 months"
        - "12 months" -> "12 months"
        - "No commitment" -> "No commitment"
        - None -> None
        """
        if not commitment:
            return None

        commitment = str(commitment).strip()

        # Handle "No commitment" case
        if 'no commitment' in commitment.lower():
            return "No commitment"

        # Extract number of months
        match = re.search(r'(\d+)\s*-?\s*month', commitment, re.IGNORECASE)
        if match:
            return f"{match.group(1)} months"

        return commitment


class EandValidationPipeline:
    """
    Pipeline for validating required fields and data quality.

    Logs warnings for:
    - Missing required fields (Name, Main_Group, Group)
    - Plans with no benefits (no data, minutes, or speed)
    - Suspicious values (price = 0, etc.)
    """

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Check required fields
        required_fields = ['Name', 'Main_Group', 'Group']
        missing_fields = [field for field in required_fields if not adapter.get(field)]

        if missing_fields:
            spider.logger.warning(
                f"⚠️  Missing required fields: {missing_fields} | "
                f"URL: {adapter.get('url', 'Unknown')}"
            )

        # Check if plan has any benefits
        benefit_fields = [
            'Speed', 'Local_Data', 'Roaming_Data', 'Minutes',  # Renamed from Local_Minutes
            'Entertainment_Packs_Data', 'Entertainment_Pack', 'UAE_WiFi_Hours'
        ]
        has_benefits = any(adapter.get(field) for field in benefit_fields)

        if not has_benefits and adapter.get('Name'):
            spider.logger.warning(
                f"⚠️  Plan has NO benefits: {adapter.get('Name')} | "
                f"URL: {adapter.get('url', 'Unknown')}"
            )

        # Check for suspicious price
        price = adapter.get('Price_Actual')
        if price == '0' or price == 0:
            spider.logger.warning(
                f"⚠️  Suspicious price (0): {adapter.get('Name')} | "
                f"URL: {adapter.get('url', 'Unknown')}"
            )

        return item


class EandDeduplicationPipeline:
    """
    Pipeline to prevent duplicate items based on Name + Main_Group + Group.

    Keeps track of seen items and drops duplicates.
    """

    def __init__(self):
        self.seen_items = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Create unique key from Name + Main_Group + Group + URL + scrape_ts
        # Using URL + timestamp ensures plans with missing names don't get dropped as duplicates
        name = adapter.get('Name') or ''
        main_group = adapter.get('Main_Group') or ''
        group = adapter.get('Group') or ''
        url = adapter.get('url') or ''
        scrape_ts = adapter.get('scrape_ts') or ''

        # Only deduplicate if we have a valid name
        # If name is empty, treat each as unique (use timestamp)
        if name:
            unique_key = f"{name}|{main_group}|{group}".lower()
        else:
            # For items without names, use URL + timestamp to avoid false duplicates
            unique_key = f"{url}|{scrape_ts}".lower()

        if unique_key in self.seen_items:
            spider.logger.info(
                f"🗑️  Dropping duplicate: {name or 'Unnamed'} ({main_group} > {group})"
            )
            # Drop the item by raising DropItem exception
            from scrapy.exceptions import DropItem
            raise DropItem(f"Duplicate item: {name or 'Unnamed'}")
        else:
            self.seen_items.add(unique_key)
            return item
