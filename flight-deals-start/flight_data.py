
class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, departure, arrive, out_date, return_date):
        self.price = price
        self.departure = departure
        self.arrive = arrive
        self.out_date = out_date
        self.return_date = return_date

def fing_cheapest_flight(data):
    first_flight = data[0]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"]
    arrive_date = first_flight["itineraries"][0]["segments"][1]["arrival"]["at"]
    departure = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    arrival = first_flight["itineraries"][0]["segments"][1]["arrival"]["iataCode"]
    lowest_price = float(first_flight["price"]["total"])

    cheapest_flight = FlightData(
        price=lowest_price,
        departure=departure,
        arrive=arrival,
        out_date=out_date,
        return_date=arrive_date
    )

    for flight in data:
        price = float(flight["price"]["total"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight


