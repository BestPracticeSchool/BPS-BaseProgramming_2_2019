import requests

response = requests.get('http://api.github.com')
if response.status_code == 200:
    print(response)
else:
    print("ERROR!")