import csv
import os
from multiprocessing import connection

from sqlalchemy.orm import sessionmaker
from bizlogic.mega_millions import create_date_mapping_tables

from datastore.connecting import get_engine
from datastore.models import create_all_tables
from datastore.models.mega_millions import (
    Days,
    DaysOfTheWeek,
    MegaBallNumbers,
    Months,
    Quarters,
    RegularNumbers,
    Weeks,
    Winners,
    Years,
)
from datastore.models.mega_millions_generated_data import ConnectedNumberOccurrences

engine_name = "mega_millions_after_2013"
engine = get_engine(name=engine_name)
Session = sessionmaker(engine)

ROOT_DIR = os.path.abspath(os.curdir)


def get_percent_for_all_numbers() -> None:
    row_list = [["Number", "Count", "Percentage"]]
    with open(
        f"{ROOT_DIR}/statistics/regular_number_stats.csv", "w", newline=""
    ) as file:
        with Session() as sess:
            count_of_all_rows = sess.query(RegularNumbers).count()
            for number in sess.query(RegularNumbers.number).distinct():
                count_for_number = (
                    sess.query(RegularNumbers)
                    .filter(RegularNumbers.number == number[0])
                    .count()
                )
                percentage = 100.0 * count_for_number / count_of_all_rows
                print(
                    f"number: {number[0]} has a count of {count_for_number} and a percentage of {percentage}"
                )
                row = [number[0], count_for_number, percentage]
                row_list.append(row)
            writer = csv.writer(file)
            writer.writerows(row_list)

    row_list = [["Number", "Count", "Percentage"]]
    with open(
        f"{ROOT_DIR}/statistics/mega_ball_number_stats.csv", "w", newline=""
    ) as file:
        with Session() as sess:
            count_of_all_rows = sess.query(MegaBallNumbers).count()
            for number in sess.query(MegaBallNumbers.number).distinct():
                count_for_number = (
                    sess.query(MegaBallNumbers)
                    .filter(MegaBallNumbers.number == number[0])
                    .count()
                )
                percentage = 100.0 * count_for_number / count_of_all_rows
                print(
                    f"number: {number[0]} has a count of {count_for_number} and a percentage of {percentage}"
                )
                row = [number[0], count_for_number, percentage]
                row_list.append(row)
            writer = csv.writer(file)
            writer.writerows(row_list)


def set_connected_number_occurrences() -> None:
    with Session() as sess:
        truncate_statement = """DROP TABLE connected_number_occurrences"""
        sess.execute(truncate_statement)
        sess.commit()
        create_all_tables(engine_name=engine_name)

        for numbers_possible in range(1, 71):
            connectedNumberOccurrences = ConnectedNumberOccurrences(
                lottery_number=numbers_possible
            )
            sess.add(connectedNumberOccurrences)
            sess.commit()

        for id in sess.query(Winners.id).distinct():
            winner_row = sess.query(Winners).filter(Winners.id == id[0]).first()
            first_number = winner_row.first_number
            second_number = winner_row.second_number
            third_number = winner_row.third_number
            fourth_number = winner_row.fourth_number
            fifth_number = winner_row.fifth_number

            add_occurrence_of_other_lotto_numbers(
                main_number=first_number,
                other_number_1=second_number,
                other_number_2=third_number,
                other_number_3=fourth_number,
                other_number_4=fifth_number,
                sess=sess,
            )

            add_occurrence_of_other_lotto_numbers(
                main_number=second_number,
                other_number_1=first_number,
                other_number_2=third_number,
                other_number_3=fourth_number,
                other_number_4=fifth_number,
                sess=sess,
            )

            add_occurrence_of_other_lotto_numbers(
                main_number=third_number,
                other_number_1=first_number,
                other_number_2=second_number,
                other_number_3=fourth_number,
                other_number_4=fifth_number,
                sess=sess,
            )

            add_occurrence_of_other_lotto_numbers(
                main_number=fourth_number,
                other_number_1=first_number,
                other_number_2=second_number,
                other_number_3=third_number,
                other_number_4=fifth_number,
                sess=sess,
            )

            add_occurrence_of_other_lotto_numbers(
                main_number=fifth_number,
                other_number_1=first_number,
                other_number_2=second_number,
                other_number_3=third_number,
                other_number_4=fourth_number,
                sess=sess,
            )


def update_recent_connected_number_occurrences() -> None:
    with Session() as sess:
        last_two_added_winners = (
            sess.query(Winners).order_by(Winners.id.desc()).limit(2)
        )
        for winner in last_two_added_winners:
            first_number = winner.first_number
            second_number = winner.second_number
            third_number = winner.third_number
            fourth_number = winner.fourth_number
            fifth_number = winner.fifth_number

            add_occurrence_of_other_lotto_numbers(
                main_number=first_number,
                other_number_1=second_number,
                other_number_2=third_number,
                other_number_3=fourth_number,
                other_number_4=fifth_number,
            )


def add_occurrence_of_other_lotto_numbers(
    main_number, other_number_1, other_number_2, other_number_3, other_number_4, sess
):
    if (
        main_number <= 70
        and other_number_1 <= 70
        and other_number_2 <= 70
        and other_number_3 <= 70
        and other_number_4 <= 70
    ):
        second_other_number = f"otherNumber{other_number_1}"
        third_other_number = f"otherNumber{other_number_2}"
        fourth_other_number = f"otherNumber{other_number_3}"
        fifth_other_number = f"otherNumber{other_number_4}"

        statement = f"UPDATE connected_number_occurrences SET {second_other_number} = {second_other_number} + 1 WHERE lottery_number = {main_number}"
        sess.execute(statement)

        statement = f"UPDATE connected_number_occurrences SET {third_other_number} = {third_other_number} + 1 WHERE lottery_number = {main_number}"
        sess.execute(statement)

        statement = f"UPDATE connected_number_occurrences SET {fourth_other_number} = {fourth_other_number} + 1 WHERE lottery_number = {main_number}"
        sess.execute(statement)

        statement = f"UPDATE connected_number_occurrences SET {fifth_other_number} = {fifth_other_number} + 1 WHERE lottery_number = {main_number}"
        sess.execute(statement)
        # Update all the columns for the first number by increment by one for second_number -> fifth_number
        #
        sess.commit()
