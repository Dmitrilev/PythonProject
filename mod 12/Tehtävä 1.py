import json
import requests

request = "https://api.chucknorris.io/jokes/random"

try:
    respons = requests.get(request)
    if respons.status_code == 200:
        respons = respons.json()
        print(respons["value"])
    else:
        print("Palvelin vastasi virhekoodilla:", respons.status_code)
except requests.exceptions.RequestException as a:
    print("Tapahtui joku virhe")

