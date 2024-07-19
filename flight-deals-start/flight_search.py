import os
from datetime import datetime
import requests
from dotenv import load_dotenv
load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITIES_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.apy_secret = os.getenv("AMADEUS_API_SECRET")
        self.token = self._get_new_token()
        self.date_time = datetime.now()
        self.date = self.date_time.strftime("%Y-%m-%d")
        self.time = self.date_time.strftime("%H:%M:%S")

    def _get_new_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        body = {
            'grant_type': 'client_credentials',
            "client_id": self.api_key,
            "client_secret": self.apy_secret,
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body, verify=False)
        token = response.json()["access_token"]
        return token

    def city_search(self, city):
        header = {"Authorization": f"Bearer {self.token}"}
        query = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=CITIES_ENDPOINT, verify=False, headers=header, params=query)
        try:
            iata_code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}")
            return "Not Found"

        return iata_code

    def find_flights(self, iata_code):
        header = {
            "Authorization": f"Bearer {self.token}",
            "X-HTTP-Method-Override": "GET",
        }
        body = {
                "currencyCode": "MXN",
                "originDestinations": [
                    {
                        "id": "1",
                        "originLocationCode": "GDL",
                        "destinationLocationCode": iata_code,
                        "departureDateTimeRange": {
                            "date": self.date,
                            "time": self.time
                        }
                    }
                ],
                "travelers": [
                    {
                        "id": "1",
                        "travelerType": "ADULT"
                    }
                ],
                "sources": [
                    "GDS"
                ],
                "searchCriteria": {
                    "maxFlightOffers": 2,
                    "flightFilters": {
                        "cabinRestrictions": [
                            {
                                "cabin": "BUSINESS",
                                "coverage": "MOST_SEGMENTS",
                                "originDestinationIds": [
                                    "1"
                                ]
                            }
                        ]
                    }
                }
            }
        response = requests.post(url=FLIGHT_ENDPOINT, headers=header, json=body, verify=False)
        # print(response.text)
        return response.json()


