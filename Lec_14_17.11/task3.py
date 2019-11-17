import requests
from requests.exceptions import HTTPError

urls = ['http://api.github.com', 'https://bestpracs.ru' ]
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print("An error was found in http part: ", http_err)
    except Exception as err:
        print("An error in urls: ", err)
    else:
        if response.status_code == 200:
            data = response.json()
            for k,v in data.items():
                new_resp = requests.get(v)
                if new_resp.status_code == 200:
                    print(k, v, new_resp.status_code)
        break
