import requests
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "d190d259afb6e0039746d99691712262"
CITY = "Vallabh Vidhyanagar"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit    

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
#sunrise_time = response['sys']['sunrise'] + response['timezone']
print(f"Temperature in {CITY} : {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Temperature in {CITY} feels like : {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {CITY} : {humidity}%")
print(f"General Weather in {CITY} : {description}")
