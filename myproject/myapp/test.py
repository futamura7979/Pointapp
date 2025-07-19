import schedule
import time
import multiprocessing

def selenium_job(getpoint):
    
    schedule.every(3).minutes.do(getpoint)

    while True:
        schedule.run_pending()
        time.sleep(1)