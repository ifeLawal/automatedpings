import datetime as dt
import sys

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from bizlogic import scrape_ipo_buzz_and_email

print(sys.path)

default_args = {
    "owner": "airflow",
    "start_date": dt.datetime(2021, 10, 20, 10, 00, 00),
    "concurrency": 1,
    "retries": 0,
}

with DAG(
    "my_simple_dag",
    default_args=default_args,
    schedule_interval="00 23 * * SUN",
) as dag:
    opr_notify = BashOperator(
        task_id="notification", bash_command="scripts/notification.sh "
    )
    opr_scrape_and_email = PythonOperator(
        task_id="", python_callable=scrape_ipo_buzz_and_email
    )

opr_scrape_and_email >> opr_notify
