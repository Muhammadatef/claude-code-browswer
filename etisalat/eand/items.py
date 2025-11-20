"""
Etisalat Plan Item Definitions

This module defines the data structure for scraped Etisalat mobile plans.
Fields are designed to match du.ae structure with additional Etisalat-specific fields.
"""

import scrapy


class EtisalatPlanItem(scrapy.Item):
    """Item representing an Etisalat mobile plan"""

    # Basic Information
    Link = scrapy.Field()
    Name = scrapy.Field()
    Description = scrapy.Field()

    # Pricing
    Price_Actual = scrapy.Field()
    Price_Original = scrapy.Field()
    Discount = scrapy.Field()

    # Categorization
    Main_Group = scrapy.Field()  # e.g., "Mobile Plans", "Home Internet"
    Group = scrapy.Field()  # e.g., "Postpaid", "Prepaid"
    Navigational_Aid = scrapy.Field()  # Breadcrumb trail

    # Benefits (up to 5 benefits per plan)
    Benefit_1 = scrapy.Field()
    Benefit_2 = scrapy.Field()
    Benefit_3 = scrapy.Field()
    Benefit_4 = scrapy.Field()
    Benefit_5 = scrapy.Field()

    # Plan Details
    Speed = scrapy.Field()  # Internet speed
    Minutes_Category = scrapy.Field()  # "Flexi (International + Local)" or "Local Only"
    Local_Minutes = scrapy.Field()
    International_Minutes = scrapy.Field()
    Data_Allowance = scrapy.Field()
    Roaming_Data = scrapy.Field()
    Commitment = scrapy.Field()  # Contract duration

    # Product Codes
    GTIN_Code = scrapy.Field()
    UAE_GTIN = scrapy.Field()
    EAN_Code = scrapy.Field()

    # Metadata
    url = scrapy.Field()
    scrape_ts = scrapy.Field()
    insert_ts = scrapy.Field()
    frequency = scrapy.Field()
    domain = scrapy.Field()
