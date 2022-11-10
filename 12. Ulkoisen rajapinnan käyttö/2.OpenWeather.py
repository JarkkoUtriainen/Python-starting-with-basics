import requests
import json

city_name = input('Give name of municipality: ')

API_key = "8b98bc01e0677287cb58624af62d1cbf"
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_key}"
response = requests.get(url)
data = json.loads(response.text)

lat = data[0]["lat"]
lon = data[0]["lon"]
url_2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
response_2 = requests.get(url_2)
data_2 = json.loads(response_2.text)

condition = data_2["weather"][0]["description"]
temp = data_2["main"]["temp"]

place = data_2["sys"]["country"]

print(f'Weather in {city_name}: {condition} with temperature of {temp}C')