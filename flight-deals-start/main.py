from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import fing_cheapest_flight

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
API_KEY = "oyrfaVxU9EKTdtAb1raCguxfP7JeRVJs"
API_SECRET = "K6DI5D4mOHqhl3tA"

datamanager = DataManager()
flightSearch = FlightSearch()
sheet_data = datamanager.get()
# for item in sheet_data:
#     item["iataCode"] = flightSearch.city_search(item["city"])

# datamanager.data = sheet_data
# datamanager.put()
print(sheet_data)
for destination in sheet_data:
    flight = flightSearch.find_flights(destination["iataCode"])
    cheapest_flight = fing_cheapest_flight(flight["data"])
    print(f"{destination["city"]}: ${cheapest_flight.price}")

