from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler


def start(getpoint1):

        scheduler = BackgroundScheduler()
        
        scheduler.add_job(getpoint1, 'interval', minutes=4)
        scheduler.start()
        