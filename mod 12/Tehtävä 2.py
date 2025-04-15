import json
import requests

city_name = input("Kirjoita paikkakunnasi: ")
request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=87bf61f1ad4bfb244c893ecd77f83a18"

respons = requests.get(request)
try:
    if respons.status_code==200:
        respons = respons.json()
        weather = respons["weather"][0]["description"]
        temp_celcius = respons["main"]["temp"]-273.15

        print(f"Säätilanne: {weather}\n"
              f"lämpötila: {temp_celcius:.1f}°C")
    else:
        print("Palvelin vastasi virhekoodilla:", respons.status_code)
except requests.exceptions.RequestException as a:
    print("Tapahtui joku virhe")
