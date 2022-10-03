import os

from crontab import CronTab

# Enter the crontab page using crontab -e

cron = CronTab(user=True)
basedir = os.path.abspath(os.path.dirname(__file__))
job = cron.new(command=os.path.join(basedir, "cron-test.sh"))
job.minute.every(1)
cron.write()
