import requests

response = requests.get('https://bestpracs.ru')
if response.status_code == 200:
    print(response.text)
    
else:
    print("ERROR!")