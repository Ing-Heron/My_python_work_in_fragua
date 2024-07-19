import os
import requests
from dotenv import load_dotenv
load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/1161be69d8e2d600e2f0f69d052796ac/flightDeals/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.data = {}

    def get(self):
        response = requests.get(url=SHEETY_ENDPOINT, verify=False, auth=(self.user, self.password))
        self.data = response.json()["prices"]
        return self.data

    def put(self):
        for item in self.data:
            print(self.data)
            new_data = {
                "price": {
                    "iataCode": item["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{item["id"]}",
                verify=False,
                json=new_data,
                auth=(self.user, self.password))
            print(response.text)
