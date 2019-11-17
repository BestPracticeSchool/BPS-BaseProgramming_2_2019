import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        response.raise_for_status()
    except HTTPError as http_err:
        print("An error was found:",http_err)
    except Exception as exc:
        print("Another error: ", exc)
    else:
        print("Success!")
