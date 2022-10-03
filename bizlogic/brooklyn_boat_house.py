# from emailsystem.emailer import EmailSystem
import requests
from lxml import etree, html

from scrape.scraper import Scraper

# import json


def see_if_kayak_slots_are_available():
    scraper = Scraper(base_url="https://www.bbpboathouse.org/")
    make_reservation_elem = "//h1[@id='make-reservation']"
    grab_parent = "/.."
    following_sibling_any_type = "/following-sibling::*"
    reservation_section_xpath = (
        make_reservation_elem + grab_parent + grab_parent + following_sibling_any_type
    )
    scraper.print_section_content(endpoint="", xpath=reservation_section_xpath)
