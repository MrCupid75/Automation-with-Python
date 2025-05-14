import schedule
import time

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def greet():
    print("Keep Going")


schedule.every().day.at("10:48").do(greet)

run_scheduler()