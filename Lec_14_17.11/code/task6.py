import requests
from bs4 import BeautifulSoup as bs

s = requests.Session()

headers = {"accept":"*/*" ,"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

response = s.get('https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=python', headers = headers)
soup = bs(response.content, "lxml")
divs = soup.find_all("div", attrs = {'data-qa':'vacancy-serp__vacancy'})
for div in divs:
    print(div.find("a", attrs = {'data-qa':"vacancy-serp__vacancy-title"}).text)
