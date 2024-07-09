import requests
from datetime import datetime

APP_ID = "0182d539"
API_KEY = "3b36dfdd3f1764f4f3917316978af19c"
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY = "https://api.sheety.co/1161be69d8e2d600e2f0f69d052796ac/workoutTracking/workouts"
now_day = datetime.today()
today_ymd = now_day.strftime("%d/%m/%Y")
time_now = now_day.strftime("%H:%M:%S")
exercise = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

app_query = {
    "query": exercise
}

response = requests.post(url=ENDPOINT, headers=headers, json=app_query, verify=False)
result = response.json()

for i in result["exercises"]:
    json_payload = {
        "workout": {
            "date": today_ymd,
            "time": time_now,
            "exercise": i["name"],
            "duration": i["duration_min"],
            "calories": i["nf_calories"],
        },
    }

    sheety = requests.post(url=SHEETY, json=json_payload, verify=False, auth=("heron", "saskia"))
    print(sheety.text)
