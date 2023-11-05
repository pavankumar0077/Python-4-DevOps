# Task Scheduling

import schedule
import time

def job():
    print("This is a scheduled task.")

# Schedule as task to run every day at 2 PM
schedule.every().day.at("13:58").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)