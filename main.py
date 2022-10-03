import os

from bizlogic import (
    mega_millions,
    ping_housing_connect_and_email,
    scrape_ipo_buzz_and_email,
)
from bizlogic.brooklyn_boat_house import see_if_kayak_slots_are_available
from bizlogic.events_in_the_city import scrape_event_pages_and_email
from bizlogic.mega_millions import (
    scrape_all_mega_millions_numbers,
    scrape_most_recent_mega_millions_number,
)

if __name__ == "__main__":
    func_to_run = os.environ["FUNC_TO_RUN"]
    if func_to_run == "ipo_buzz":
        scrape_ipo_buzz_and_email()
    if func_to_run == "mega_millions":
        scrape_most_recent_mega_millions_number()
    if func_to_run == "events":
        scrape_event_pages_and_email()
    else:
        ping_housing_connect_and_email()
