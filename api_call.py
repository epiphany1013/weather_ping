import json
import time
import requests
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

while (True):
    for city in cities:
        city_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&lang=kr&units=metric"
        response = requests.get(city_url)
        parsed_data = json.loads(response.text)
        if (previous_weather[index % 2] != parsed_data['weather'][0]['description']): # 이전 날씨와 다를 경우만 아래 코드 실행
            message = {
                "message": f"{city:15}  {parsed_data['weather'][0]['description']}" #라인에 보낼 message 구성
            }
            requests.post(api_url, headers=headers, data=message) # LINE api에 POST method로 메시지 보냄
        previous_weather[index % 2] = parsed_data['weather'][0]['description'] # 받아온 날씨 정보를 pasring 해서 이전 날씨 데이터에 넣어줌.
        # print(f"{city:15}  {parsed_data['weather'][0]['description']}")
        index += 1
    time.sleep(600) # 10분 간격으로 loop 순회
