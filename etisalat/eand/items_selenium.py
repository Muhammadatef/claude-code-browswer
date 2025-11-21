"""
Etisalat Plan Item Definitions for Selenium Spider

This module defines the data structure for scraped Etisalat mobile plans
using Selenium-based extraction with complete field coverage.

Author: Mohamed Atef Fahmi
Date: 2025-11-21
"""

import scrapy


class EtisalatPlanItem(scrapy.Item):
    """Item representing an Etisalat mobile plan with complete field coverage"""

    # Product Information
    Link = scrapy.Field()  # Category URL (all plans in subcategory share same link)
    Name = scrapy.Field()  # Plan name

    # Pricing
    Price_Actual = scrapy.Field()  # Current price (e.g., "AED 199/month")

    # Categorization
    Main_Group = scrapy.Field()  # e.g., "Mobile Plans", "Home Internet"
    Group = scrapy.Field()  # e.g., "Postpaid", "Prepaid", "Visitor"
    Navigational_Aid = scrapy.Field()  # Full breadcrumb (e.g., "Mobile Plans > Postpaid > Freedom Entertainment Plans")

    # Core Benefits
    Speed = scrapy.Field()  # Internet speed (e.g., "1 Gbps", "300 Mbps")
    Local_Data = scrapy.Field()  # Local data allowance (e.g., "Unlimited", "50 GB")
    Roaming_Data = scrapy.Field()  # Roaming data allowance
    Minutes = scrapy.Field()  # Local minutes (renamed from Local_Minutes)
    Minutes_Category = scrapy.Field()  # "Flexi (Local & Int'l)" or "Local Only"

    # Unique Plan Features (Variable benefit fields)
    Variable = scrapy.Field()  # Unique feature name (e.g., "Intl' Calls to 1 Preferred Number")
    Variable_value = scrapy.Field()  # Unique feature value (e.g., "Unlimited")

    # Entertainment & WiFi
    Entertainment_Packs_Data = scrapy.Field()  # Data for entertainment packs
    Entertainment_Pack = scrapy.Field()  # Entertainment pack name (e.g., "Netflix", "OSN+")
    UAE_WiFi_Hours = scrapy.Field()  # UAE WiFi hours

    # Additional Benefits
    Additional_Benefits = scrapy.Field()  # Pipe-separated list of additional benefits

    # Contract & Promotions
    Promotion = scrapy.Field()  # Active promotions
    Commitment = scrapy.Field()  # Contract duration (e.g., "12 months", "No commitment")

    # Product Codes
    GTIN_Code = scrapy.Field()  # Global Trade Item Number
    UAE_GTIN = scrapy.Field()  # UAE-specific GTIN
    EAN_Code = scrapy.Field()  # European Article Number

    # Metadata
    url = scrapy.Field()  # Source URL
    scrape_ts = scrapy.Field()  # Scrape timestamp
    insert_ts = scrapy.Field()  # Database insert timestamp
    frequency = scrapy.Field()  # Scraping frequency (e.g., "daily")
    domain = scrapy.Field()  # Domain name (e.g., "etisalat.ae")
