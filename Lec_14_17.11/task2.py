import requests
from requests.exceptions import HTTPError

urls = ['http://api.github.com', 'https://bestpracs.ru', 'http://api.github.com/qwerty' ]

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print("An error was found in http part: ", http_err)
    except Exception as err:
        print("An error in urls: ", err)
    else:
        print(url, response.status_code)
    

