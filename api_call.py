import json
import time
import requests
from datetime import datetime
from api_key import line_key, weather_key

cities = [
    "Suwon-si",
    "Pohang",
]
api_url = "https://notify-api.line.me/api/notify"

headers = {'Authorization': 'Bearer ' + line_key}

previous_weather = [
    "기존 날씨",
    "기존 날씨",
]
index = 0
last_executed_day = None
while True:
    current_time = datetime.now()
    if current_time.hour == 11 and (last_executed_day is None or last_executed_day != current_time.date()):
        for city in cities:
            city_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&lang=kr&units=metric"
            response = requests.get(city_url)
            parsed_data = json.loads(response.text)

            message = {
                "message": f"{city:<15} \n"
                           f"현재 온도는 {str(parsed_data['main']['temp'])}\n" +
                           f"체감 온도는 {str(parsed_data['main']['feels_like'])}\n" +
                           f"최고 온도는 {str(parsed_data['main']['temp_max'])}\n" +
                           f"최저 온도는 {str(parsed_data['main']['temp_min'])}\n" +
                           f"현재 습도는 {str(parsed_data['main']['humidity'])}\n"
            }
            requests.post(api_url, headers=headers, data=message)
        last_executed_day = current_time.date()

    for index, city in enumerate(cities):
        city_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&lang=kr&units=metric"
        response = requests.get(city_url)
        parsed_data = json.loads(response.text)

        if previous_weather[index] != parsed_data['weather'][0]['description']:
            message = {"message": f"{city:15}\n  {parsed_data['weather'][0]['description']}"}
            requests.post(api_url, headers=headers, data=message)
            previous_weather[index] = parsed_data['weather'][0]['description']

    time.sleep(10)

