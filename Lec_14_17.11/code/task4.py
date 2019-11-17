import requests
from requests.exceptions import HTTPError
try:
    response = requests.get('https://api.github.com')
    response.raise_for_status()
except HTTPError as http_err:
    print("An error was found:", http_err)
except Exception as err:
    print("An error was found:", err)
else:
    print("Success!")
    print(response.content)
    print("###########################")
    print(type(response.text))
    print(response.json())
    print("###########################")
    print(response.headers['Date'])
