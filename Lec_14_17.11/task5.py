import requests as r 
from bs4 import BeautifulSoup as bs 
target = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=golang'
session = r.Session()
headers = {'accept': '*/*' , 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/78.0.3904.97 Chrome/78.0.3904.97 Safari/537.36'}
response = session.get(target, headers = headers)
if response.status_code == 200:
    soup = bs(response.content, 'lxml')
    divs = soup.find_all("div", attrs = {"data-qa" : "vacancy-serp__vacancy"})
    for div in divs:
        title = div.find("a", attrs={"data-qa":"vacancy-serp__vacancy-title"}).text 
        print(title)
else:
    print("ERROR", response.status_code)
