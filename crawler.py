# imports
import scrapper
import sys
from datetime import datetime, timedelta
from time import sleep
from fake_useragent import UserAgent

def startCrawling(date1, date2):
    agents = UserAgent()
    print("Crawling started for date range ", date1.strftime('%d-%m-%Y'), ' to ', date2.strftime('%d-%m-%Y'))
    if date1 > date2:
        temp = date1
        date1 = date2
        date2 = temp
    pagenumber = 1
    request_number = 0
    agent = agents.random
    while date1 <= date2:
        request_number += 1
        currenturl = 'https://www.prothomalo.com/archive/'+date1.strftime('%Y-%m-%d')+'?page='+str(pagenumber)
        print("Currently fetching address: ", currenturl)        
        nextpage = scrapper.scrap(currenturl, date1.strftime('%Y-%m-%d'), agent)
        if nextpage:
            pagenumber += 1
        else:
            pagenumber = 1
            agent = agents.random
            date1 = date1 + timedelta(days=1)
        sleep(0.3)
        if request_number == 50:
            sleep(10)
            request_number = 0
    print("ended")

# to provide parameter directly from terminal
if len(sys.argv) >= 3:
    date1 = datetime.strptime(sys.argv[1], '%d.%m.%Y').date()
    date2 = datetime.strptime(sys.argv[2], '%d.%m.%Y').date()
    startCrawling(date1, date2)
else:
    print('Enter date from(dd.mm.yyyy): ', end='')
    a = str(input())
    print('Enter date to(dd.mm.yyyy): ', end='')
    b = str(input())
    date1 = datetime.strptime(a, '%d.%m.%Y').date()
    date2 = datetime.strptime(b, '%d.%m.%Y').date()
    startCrawling(date1, date2)    