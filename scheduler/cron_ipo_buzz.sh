#!/bin/bash
dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
python=/Users/ifeoluwalawal/.virtualenvs/scrape-and-email/bin/python
notifier=/usr/local/bin/terminal-notifier

cd $dir
export FUNC_TO_RUN="ipo_buzz"
$python ../main.py
$notifier -title "Ran IPO_Scoop_and_Email" -subtitle "Scrape and Email Ran" -message "Completed"
now=$(date)
echo "Cron job completed at $now"