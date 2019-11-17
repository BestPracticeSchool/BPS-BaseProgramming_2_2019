import requests
from getpass import getpass 

response = requests.get('https://api.github.com/')
data = response.json()
for k,v in data.items():
    new_response = requests.get(v)
    if new_response.status_code == 200:
        print(k, v)

emo_resp = requests.get('https://api.github.com/emojis')
print(emo_resp.content)