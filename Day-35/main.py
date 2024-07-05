import os
import requests
from twilio.rest import Client

# RECOVERY_CODE = "9EM5TRHPVWY915CD3MUG691H"
account_sid = "Your sid"
auth_token = "Your token"
# auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWN_API_KEY")

city = {
    "cancun": {
        "lat": 21.161907,
        "lon": -86.851524,
    },
    "zapopan": {
        "lat": 20.697798462513493,
        "lon": -103.37288494157396,
    },
    "monterrey": {
        "lat": 25.686613,
        "lon": -100.316116
    },
}

param = {
    "lat": city["monterrey"]["lat"],
    "lon": city["monterrey"]["lon"],
    "appid": "df5e73e7cd50d3cbb6102759a3aebbf1",
    "cnt": 4,
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=param)
response.raise_for_status()
json_response = response.json()
weather_list = json_response["list"]
weather_ids = [id["weather"][0]["id"] for id in weather_list]
will_rain = False
for ids in weather_ids:
    if ids <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, Remember to bring an umbrella ☔",
        from_="+523312457889",
        to="+523317025175",
    )
# In the terminal we going to add:
# export OWN_API_KEY=df5e73e7cd50d3cbb6102759a3aebbf1
# export AUTH_TOKEN=
