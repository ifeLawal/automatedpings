import random
from bizlogic.mega_millions import Session
from datastore.models.mega_millions_generated_data import PureRandomTicketAttempts
from datetime import date

number_of_tickets_to_make = 30
regular_numbers_needed = 5


def create_wednesday_tickets():
    date.today()


def create_thirty_tickets(date: date) -> None:
    for _ in number_of_tickets_to_make:
        arr = pick_numbers()
        arr.append(pick_mega_ball())
        with Session() as session:
            new_ticket = PureRandomTicketAttempts(
                draw_date=date.today(),
                first_number=arr[0],
                second_number=arr[1],
                third_number=arr[2],
                fourth_number=arr[3],
                fifth_number=arr[4],
                mega_ball=arr[5],
            )
            session.add(new_ticket)
            session.commit()


def pick_numbers() -> list:
    return random.sample(range(1, 70), regular_numbers_needed)


def pick_mega_ball() -> int:
    return random.randint(1, 25)
