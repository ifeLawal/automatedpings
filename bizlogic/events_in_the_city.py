from lxml import etree, html

from emailsystem.emailer import EmailSystem
from navigators.page_navigator import PageNavigator
from scrape.scraper import Scraper

nyu_events_url = (
    "https://events.alumni.nyu.edu/c/calendar/556ea019-a65e-477c-a70b-8d09c3af966c"
)

nyu_navigator = PageNavigator(
    url=nyu_events_url, inputs={"point_of_interest": "New York"}
)


def scrape_event_pages_and_email():
    # NYU
    nyu_navigator.setup_method()
    nyu_navigator.wait_to_load(2)
    nyu_navigator.fill_input(
        xPath="//input[@id='9a9a7027-8eda-43e0-873a-3ddc2191daee']",
        keys="New York, NY, USA",
    )
    nyu_navigator.wait_to_load(1)
    nyu_navigator.click(xPath="//li[@class='LocationFilter__suggestion___siwNc'][1]")
    nyu_navigator.wait_to_load(1)
    show_more_button = nyu_navigator.check_if_element_is_on_page(
        xPath="//div[@id='calendarList_showMore']"
    )
    if show_more_button:
        nyu_navigator.scroll_to_element(xPath="//div[@id='calendarList_showMore']")
        nyu_navigator.wait_to_load(1)
        show_more_button.click()
    nyu_navigator.wait_to_load(1)
    nyu_navigator.scroll_to_bottom_of_page()
    all_events = nyu_navigator.check_if_element_is_on_page(
        xPath="//div[@class='CalendarViewWidget__mainContainer___2ouCB']"
    )
    
    full_html_content = nyu_navigator.get_element_innerhtml(element=all_events).encode('ascii', "ignore")

    nyu_navigator.teardown_method()
    
    # Hacienda
    
    
    
    # Eventbrite
    
    
    
    # BBP
    
    emailSystem = EmailSystem()
    emailSystem.sendEmail(
        recipients=["ifelaw2439@gmail.com"],
        subject="NYC Events",
        message_html=full_html_content,
    )