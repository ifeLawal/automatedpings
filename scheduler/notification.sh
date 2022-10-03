#!/bin/bash

notifier=/usr/local/bin/terminal-notifier

$notifier -title "Test cron" -subtitle "Appending succeeded" -message "Completed"
now=$(date)
echo "Cron job completed at $now"