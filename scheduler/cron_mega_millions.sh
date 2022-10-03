#!/bin/bash
dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
python=/Users/ifeoluwalawal/.virtualenvs/scrape-and-email/bin/python
notifier=/usr/local/bin/terminal-notifier

cd $dir
export FUNC_TO_RUN="mega_millions"
$python ../main.py
$notifier -title "Ran mega millions scrape" -subtitle "Scraped bruh" -message "Completed"
now=$(date)
echo "Cron job completed at $now"