import requests
from datetime import datetime

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "USDMXN",
    "apikey": "6A4PQ3XX6MOY1JXJ"
}

response = requests.get(url="https://www.alphavantage.co/query", params=params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

date_ = datetime.now()
today_date = str(date_.date())

dolar_today = float(data[today_date]["4. close"])
print(dolar_today)

if dolar_today <= 17:
    print("Dollar is cheap")
