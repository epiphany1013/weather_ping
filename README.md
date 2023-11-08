# 날씨 알림 프로젝트

📌 개요

이 프로젝트는 OpenWeatherMap API를 통해 실시간으로 날씨 정보를 수집하고, LINE API를 사용하여 날씨 변경 사항을 알림으로 전송합니다. 사용자는 다양한 도시의 날씨 정보를 주기적으로 받을 수 있으며, 날씨 변화가 감지될 때마다 즉시 알림을 받게 됩니다.


📌 기능
- 여러 도시의 실시간 날씨 정보 수집
- 날씨 변화 감지 시 LINE을 통한 알림 전송
- 매일 아침 시간 현재 온도, 습도, 바람 속도 등의 상세 날씨 정보 제공
- 사용자 지정 도시 및 알림 설정 기능

📌 작동 환경
- Python 3.x
- OpenWeatherMap API 토큰
- LINE API 토큰

📌 설치 방법
- 이 프로젝트를 클론
```
git clone https://github.com/epiphany1013/weather_ping.git
```
- 필요한 라이브러리를 설치
```
pip install -r requirements.txt
```

- api_key.py 파일에서 사용자 개인의 토큰을 입력
```
line_key = "YOUR_TOKEN"
weather_key = "YOUR_TOKEN"
```

- 실행
스크립트를 실행하여 날씨 정보 수집 및 알림 서비스를 시작할 수 있습니다.

```
python api_call.py
```