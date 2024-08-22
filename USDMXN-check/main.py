import requests
from datetime import datetime, timedelta

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
yesterday_date = date_.today() - timedelta(days=1)

try:
    dollar_today = float(data[today_date]["4. close"])
    dollar_yesterday = float(data[str(yesterday_date.date())]["4. close"])
except KeyError:
    data_ = [item for key, item in data.items()]
    dollar_today = float(data_[0]["4. close"])
    dollar_yesterday = float(data_[1]["4. close"])

print(f"Today Dollar: {dollar_today}")
print(f"Yesterday Dollar: {dollar_yesterday}")
difference = round(dollar_yesterday - dollar_today, 4)

if difference >= 0:
    print(f"Dollar downs price: -{difference}")
else:
    print(f"Dollar raise price: +{abs(difference)}")

if dollar_today <= 17:
    print("Dollar is cheap")

price_usd = float(input("Input the price in USD: "))
price_mx = price_usd * dollar_today
print(f"USD: {price_usd} is  MXN: {price_mx}")

