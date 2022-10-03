import json

from lxml import etree, html

from emailsystem.emailer import EmailSystem
from scrape.scraper import Scraper


def scrape_ipo_buzz_and_email():
    scraper = Scraper(base_url="https://www.iposcoop.com")
    endpoints = scraper.get_website_endpoints_from_page(
        endpoint="/category/ipo-buzz", inner_tag="//div[@id='content']"
    )
    header_text = scraper.get_direct_text(
        endpoint=endpoints[0], inner_tag="//h1[@class='entry-title']"
    )
    full_html_content = scraper.get_page_content(
        endpoint=endpoints[0], inner_tag="//div[@id='content']", include_html=True
    )
    emailSystem = EmailSystem()
    emailSystem.sendEmail(
        recipients=["ifelaw2439@gmail.com"],
        subject=header_text,
        message_html=full_html_content,
    )


def ping_housing_connect_and_email():
    scraper = Scraper(base_url="https://a806-housingconnectapi.nyc.gov")
    endpoint = "/HPDPublicAPI/api/Lottery/SearchLotteries"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
    }
    # postPayload = "{\"UnitTypes\":[],\"NearbyPlaces\":[],\"NearbySubways\":[],\"Amenities\":[],\"Boroughs\":[],\"Neighborhoods\":[],\"HouseholdSize\":null,\"Income\":\"\",\"HouseholdType\":1,\"OwnerTypes\":[],\"Min\":null,\"Max\":null}"
    postPayload = {
        "UnitTypes": [],
        "NearbyPlaces": [],
        "NearbySubways": [],
        "Amenities": [],
        "Boroughs": [],
        "Neighborhoods": [],
        "HouseholdSize": None,
        "Income": "",
        "HouseholdType": 1,
        "OwnerTypes": [],
        "Min": None,
        "Max": None,
    }
    # dict = json.loads(postPayload)

    raw_json_data = scraper.get_data_using_a_request(
        endpoint=endpoint, postPayload=postPayload, headers=headers, request_type="POST"
    )
    homes_for_sale_count = len(raw_json_data["sales"])
    print(homes_for_sale_count)
    content = """<h1>Current homes for sale {}.</h1>\n
                 <code>JSON payload: {}.\n</code>
                 <p>The housingconnect website: https://housingconnect.nyc.gov/PublicWeb/search-lotteries</p>
              """.format(
        homes_for_sale_count, raw_json_data["sales"]
    )

    emailSystem = EmailSystem()
    emailSystem.sendEmail(
        recipients=["ifelaw2439@gmail.com"],
        subject="Housing Connect has {} homes for sale".format(homes_for_sale_count),
        message_html=content,
    )


def find_stock_tickers(text):
    # TODO look through the text
    # 1. find the stocks
    # 2. in a different function: find the endpoints for those stocks to see their potential pricing and links
    print("To be done")
