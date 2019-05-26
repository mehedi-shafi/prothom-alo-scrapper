import urllib.request
from bs4 import BeautifulSoup
import io

def scrap(address, date):
    request = urllib.request.Request(
        address,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    page = urllib.request.urlopen(request)
    soup = BeautifulSoup(page,"html.parser")
    title = soup.find_all("span",attrs={"class":"title"})

    with io.open('output/'+date+'.txt', 'a', encoding='utf-8') as file:
        for i in title:
            file.write(i.get_text())
            file.write('\n')
            # print(i.get_text(),"\n")
    if len(title) < 20:
        return False
    return True