from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler


def start(getpoint1):

        scheduler = BackgroundScheduler()
        
        scheduler.add_job(getpoint1, 'interval', seconds=500) # schedule
        scheduler.start()
        