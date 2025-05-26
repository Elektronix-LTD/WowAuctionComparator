from playwright.sync_api import sync_playwright
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote
import json
import sys
import time

def fetch_realms(region):
    # Use a breakpoint in the code line below to debug your script.

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://wowauction.us/eu/doomhammer/Green%20Lumberjack%20Shirt")
        page.click("button.fc-button.fc-cta-consent.fc-primary-button")
        page.click("select[name='realm[region]']")
        page.select_option("select[name='realm[region]']", region)
        rows = []
        tries = 0
        while len(rows) <= 1:
            tries += 1
            rows = page.query_selector_all("select[name='realm[server]'] > option")
            time.sleep(1)
            if tries > 5:
                break

        result = []
        for row in rows:
            if row.get_attribute("value") == '':
                continue
            result.append(row.get_attribute("value"))
        return result


def fetch_prices(region, realm, item):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Checking prices of the item in realm {realm}...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://wowauction.us/{region}/{realm}/{item}")
        page.click("button.fc-button.fc-cta-consent.fc-primary-button")
        page.select_option("select[name='realm[region]']", region)
        page.select_option("select[name='realm[server]']", realm)
        page.fill("input[name='realm[item]']", "Green Lumberjack Shirt")
        rows = []
        tries = 0
        while rows == []:
            tries += 1
            rows = page.query_selector_all("#search-container div.flex.flex-row.top-border")
            time.sleep(1)
            if tries > 5:
                break

        result = []
        for row in rows:
            item_name = row.query_selector(".text-xl").inner_text()
            link = row.query_selector(".text-xl > a").get_attribute("href")
            item_price = row.query_selector(".items-baseline div:nth-child(2)").inner_text()
            item_price = item_price.replace(",", "").split()
            item_price = {
                "gold": int(item_price[0]),
                "silver": int(item_price[1]),
                "copper": int(item_price[2])
            }
            result += [{"item_name": item_name, "link": link, "realm": realm, "item_price": item_price}]
        print(f"Finished checking prices of the item in realm {realm}...")
        return result


def make_single_price(price_object):
    return price_object["gold"] * 10000 + price_object["silver"] * 100 + price_object["copper"]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # First argument is always the script name!
    number_of_realms_to_check = -1
    if len(sys.argv) > 1:
        item_name = sys.argv[1]
        print(f"Comparing prices for: {item_name}")
    else:
        print(f"\r\nWOW Auction Comparator Tool\r\n------------------------------\r\nSyntax for running this amazing magic command:\r\n\r\npython {sys.argv[0]} \"Green Lumberjack Shirt\" 5\r\n\r\nWhere 5 is OPTIONAL and it can be any number to limit number of realms to check (if You are impatient and You don't want to wait ages till script will finish checking all 267 realms ;-)\r\n\r\n")
        sys.exit(1)

    if len(sys.argv) > 2:
        number_of_realms_to_check = int(sys.argv[2])
        print(f"Limiting number of realms to: {number_of_realms_to_check}")

    item_name = quote(item_name)
    region = "eu"
    print(f"Checking prices in following '{region}' realms:")
    realms = fetch_realms(region)

    # Limiting number of realms if user wishes that
    if number_of_realms_to_check > -1:
        realms = realms[:number_of_realms_to_check]

    print(realms)


    aggregator_by_item_name = {}
    #print(f"Prices in realm doomhammer: {json.dumps(fetch_prices(region, 'doomhammer', item_name), indent=2)}")

    tasks = [(region, realm, item_name) for realm in realms]  # 267 items!
    try:
        with ThreadPoolExecutor(max_workers=25) as executor:
            futures = [executor.submit(fetch_prices, r, re, i) for r, re, i in tasks]

            for future in as_completed(futures):
                result = future.result()
                try:
                    if len(result) > 0:
                        #print(f"Prices in realm {result[0]['realm']}: {json.dumps(result, indent=2)}")
                        for item in result:
                            # If element already exist
                            if item['item_name'] in aggregator_by_item_name:
                                # If price of currently processed item is lower than the price saved as the lowest, overwrite the saved item
                                if make_single_price(item['item_price']) < make_single_price(aggregator_by_item_name[item['item_name']]['item_price']):
                                    aggregator_by_item_name[item['item_name']] = item
                            else: # if the cheapest element is still not saved, save currently processed one:
                                aggregator_by_item_name[item['item_name']] = item
                except:
                    print(f"Error during processing.")
            print("----------------------------------------------------------------------------")
            print("""
      _____                 _ _       
     |  __ \               | | |      
     | |__) |___  ___ _   _| | |_ ___ 
     |  _  // _ \/ __| | | | | __/ __|
     | | \ \  __/\__ \ |_| | | |_\____ 
     |_|  \_\___||___/\__,_|_|\__|___/
    
            """)

            print(f"Lowest prices found for the item '{item_name}' among all ({number_of_realms_to_check}) requested realms:")
            print(json.dumps(aggregator_by_item_name, indent=2))

    except KeyboardInterrupt:
      print("\r\nnCTRL+C pressed - stopping all threads...\r\n")
