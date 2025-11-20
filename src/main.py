"""Module defines the main entry point for the Apify Actor.

This Actor scrapes du postpaid and prepaid mobile plans from du.ae website.
"""

from __future__ import annotations

from apify import Actor
from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext


async def main() -> None:
    """Define a main entry point for the Apify Actor.

    This coroutine is executed using `asyncio.run()`, so it must remain an asynchronous function for proper execution.
    Asynchronous execution is required for communication with Apify platform, and it also enhances performance in
    the field of web scraping significantly.
    """
    async with Actor:
        # Retrieve the Actor input, and use default values if not provided.
        actor_input = await Actor.get_input() or {}

        # Define start URLs for du postpaid and prepaid plans
        start_urls = actor_input.get(
            'start_urls',
            [
                {'url': 'https://shop.du.ae/en/personal/postpaid/emirati-plans'},
                {'url': 'https://shop.du.ae/en/personal/s-du-postpaid-plans'},
                {'url': 'https://shop.du.ae/en/personal/s-du-metallic-plans?showLoader=true'},
                {'url': 'https://shop.du.ae/en/personal/s-du-prepaid-flexi-plans'},
                {'url': 'https://shop.du.ae/en/personal/s-du-prepaid-easy-plans'},
            ],
        )

        # Exit if no start URLs are provided.
        if not start_urls:
            Actor.log.info('No start URLs specified in Actor input, exiting...')
            await Actor.exit()

        # Extract URL strings from the start_urls dictionaries
        # The input schema returns URLs as [{'url': '...'}, ...] but crawler expects plain strings
        urls = [url.get('url') if isinstance(url, dict) else url for url in start_urls]

        # Create a crawler.
        crawler = PlaywrightCrawler(
            max_requests_per_crawl=50,
            headless=actor_input.get('headless', True),
            browser_launch_options={
                'args': ['--disable-gpu', '--no-sandbox'],
            },
        )

        # Define a request handler for scraping plan data.
        @crawler.router.default_handler
        async def request_handler(context: PlaywrightCrawlingContext) -> None:
            url = context.request.url
            Actor.log.info(f'Scraping {url}...')

            # Wait for the page to load completely
            await context.page.wait_for_load_state('networkidle')

            # Wait a bit more for dynamic content to render
            await context.page.wait_for_timeout(3000)

            # Determine Main_Group based on URL
            main_group = None
            if 'postpaid' in url.lower():
                main_group = 'Postpaid plans'
            elif 'prepaid' in url.lower():
                main_group = 'Prepaid plans'

            # Try to extract Main_Group from page if available
            try:
                main_group_element = await context.page.query_selector('a.link')
                if main_group_element:
                    main_group_text = await main_group_element.text_content()
                    if main_group_text:
                        main_group = main_group_text.strip()
            except Exception as e:
                Actor.log.warning(f'Could not extract main group from page: {e}')

            # Extract the active group/tab (Power Plans, Smart Plans, etc.)
            group = None
            try:
                active_tab = await context.page.query_selector('.v-tab.v-tab--active')
                if active_tab:
                    group_text = await active_tab.text_content()
                    if group_text:
                        group = group_text.strip()
            except Exception as e:
                Actor.log.warning(f'Could not extract group: {e}')

            # Find all plan cards on the page
            plan_cards = await context.page.query_selector_all('.v-card, [class*="plan-card"]')

            Actor.log.info(f'Found {len(plan_cards)} plan cards on {url}')

            for card in plan_cards:
                try:
                    # Extract Name (h4 with class text-h6 white--text)
                    name = None
                    try:
                        name_element = await card.query_selector('h4.text-h6.white--text, .text-h6.white--text')
                        if name_element:
                            name_text = await name_element.text_content()
                            if name_text:
                                name = name_text.strip()
                    except Exception as e:
                        Actor.log.debug(f'Could not extract name: {e}')

                    # Skip if no name found (not a valid plan card)
                    if not name:
                        continue

                    Actor.log.info(f'Extracting plan: {name}')

                    # Extract Description
                    description = None
                    try:
                        desc_element = await card.query_selector('.d-flex.flex-row.justify-center.align-center')
                        if desc_element:
                            desc_text = await desc_element.text_content()
                            if desc_text:
                                description = desc_text.strip()
                    except Exception as e:
                        Actor.log.debug(f'Could not extract description: {e}')

                    # Extract Price_Actual (class text-h5)
                    price_actual = None
                    try:
                        price_element = await card.query_selector('.text-h5')
                        if price_element:
                            price_text = await price_element.text_content()
                            if price_text:
                                price_actual = price_text.strip()
                    except Exception as e:
                        Actor.log.debug(f'Could not extract actual price: {e}')

                    # Extract Price_Original (span with class text-decoration-line-through)
                    price_original = None
                    try:
                        original_price_element = await card.query_selector('span.text-decoration-line-through, .text-decoration-line-through.text--h6')
                        if original_price_element:
                            original_price_text = await original_price_element.text_content()
                            if original_price_text:
                                price_original = original_price_text.strip()
                    except Exception as e:
                        Actor.log.debug(f'Could not extract original price: {e}')

                    # Extract Discount
                    discount = None
                    try:
                        # Look for discount text
                        discount_elements = await card.query_selector_all('.text-overline.white--lighten80.text-truncate')
                        for elem in discount_elements:
                            text = await elem.text_content()
                            if text and ('save' in text.lower() or '%' in text.lower() or 'month' in text.lower()):
                                discount = text.strip()
                                break
                    except Exception as e:
                        Actor.log.debug(f'Could not extract discount: {e}')

                    # Extract Benefits (1-5)
                    benefits = []
                    try:
                        benefit_elements = await card.query_selector_all('.text-overline.text-truncate')
                        for elem in benefit_elements:
                            text = await elem.text_content()
                            if text:
                                benefit_text = text.strip()
                                # Filter out discount text if it appears in benefits
                                if benefit_text and benefit_text != discount:
                                    benefits.append(benefit_text)
                    except Exception as e:
                        Actor.log.debug(f'Could not extract benefits: {e}')

                    # Assign benefits to separate fields
                    benefit_1 = benefits[0] if len(benefits) > 0 else None
                    benefit_2 = benefits[1] if len(benefits) > 1 else None
                    benefit_3 = benefits[2] if len(benefits) > 2 else None
                    benefit_4 = benefits[3] if len(benefits) > 3 else None
                    benefit_5 = benefits[4] if len(benefits) > 4 else None

                    # Extract Commitment
                    commitment = None
                    try:
                        commitment_elements = await card.query_selector_all('.text-overline.white--lighten80.text-truncate.mb-1')
                        for elem in commitment_elements:
                            title = await elem.get_attribute('title')
                            if title and 'contract' in title.lower():
                                commitment = title.strip()
                                break
                            # If no title, check text content
                            if not commitment:
                                text = await elem.text_content()
                                if text and 'contract' in text.lower():
                                    commitment = text.strip()
                    except Exception as e:
                        Actor.log.debug(f'Could not extract commitment: {e}')

                    # Extract GTIN_Code, UAE_GTIN, EAN_Code
                    # These are usually not visible on the page but might be in data attributes or meta tags
                    gtin_code = None
                    uae_gtin = None
                    ean_code = None

                    try:
                        # Check for GTIN in data attributes
                        gtin_attr = await card.get_attribute('data-gtin')
                        if gtin_attr:
                            gtin_code = gtin_attr

                        # Check for EAN in data attributes
                        ean_attr = await card.get_attribute('data-ean')
                        if ean_attr:
                            ean_code = ean_attr

                        # Check for UAE GTIN
                        uae_gtin_attr = await card.get_attribute('data-uae-gtin')
                        if uae_gtin_attr:
                            uae_gtin = uae_gtin_attr

                        # Also check in the entire page HTML for these codes
                        card_html = await card.inner_html()
                        if 'gtin' in card_html.lower() and not gtin_code:
                            # Try to extract GTIN from HTML
                            Actor.log.debug('GTIN might be present in HTML but not in standard attributes')
                        if 'ean' in card_html.lower() and not ean_code:
                            Actor.log.debug('EAN might be present in HTML but not in standard attributes')
                    except Exception as e:
                        Actor.log.debug(f'Could not extract product codes: {e}')

                    # Construct the data object
                    data = {
                        'Name': name,
                        'Description': description,
                        'Price_Actual': price_actual,
                        'Price_Original': price_original,
                        'Discount': discount,
                        'Main_Group': main_group,
                        'Group': group,
                        'Benefit_1': benefit_1,
                        'Benefit_2': benefit_2,
                        'Benefit_3': benefit_3,
                        'Benefit_4': benefit_4,
                        'Benefit_5': benefit_5,
                        'Commitment': commitment,
                        'GTIN_Code': gtin_code,
                        'UAE_GTIN': uae_gtin,
                        'EAN_Code': ean_code,
                        'Source_URL': url,
                    }

                    # Store the extracted data
                    await context.push_data(data)
                    Actor.log.info(f'Successfully extracted data for plan: {name}')

                except Exception as e:
                    Actor.log.error(f'Error extracting plan data: {e}')
                    continue

            # Try to find and click on different tabs/groups to get all plans
            try:
                tabs = await context.page.query_selector_all('.v-tab')
                Actor.log.info(f'Found {len(tabs)} tabs on the page')

                for i, tab in enumerate(tabs):
                    try:
                        # Check if tab is not already active
                        tab_classes = await tab.get_attribute('class')
                        if 'v-tab--active' not in tab_classes:
                            Actor.log.info(f'Clicking tab {i+1}')
                            await tab.click()
                            await context.page.wait_for_timeout(2000)

                            # After clicking, re-run extraction for new plans
                            # This is a simplified approach; you might want to extract this into a function
                            Actor.log.info('Tab clicked, waiting for content to load...')
                    except Exception as e:
                        Actor.log.warning(f'Could not click tab {i+1}: {e}')
            except Exception as e:
                Actor.log.warning(f'Could not process tabs: {e}')

        # Run the crawler with the starting requests.
        await crawler.run(urls)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
