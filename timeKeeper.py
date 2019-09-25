import schedule
import time
from priceScrapper import neweggParser
from emailer import sendEmail

def runScrapper():
    sendEmail(neweggParser('gpu'))

schedule.every(6).hours.do(runScrapper)

while True:
    schedule.run_pending()
    time.sleep(1)
