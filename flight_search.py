import requests
from datetime import datetime, timedelta
from flight_data import FlightData


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_headers = {
            "apikey": "oORtdjjo5DIbjrtk2id6Yu6gfUlvyvli",
        }

    def get_IATA_code(self, city: str):
        """Returns a city's IATA code from city name"""
        tequila_endpoint = "https://tequila-api.kiwi.com/locations/query"
        tequila_params = {
            "term": city,
        }
        response = requests.get(url=tequila_endpoint, params=tequila_params, headers=self.tequila_headers)
        response.raise_for_status()
        iata_code = response.json()['locations'][0]['code']
        return iata_code

    def find_flight(self, iata_code: str):
        current_date = datetime.now().strftime("%d/%m/%Y")
        latest_date = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")

        tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
        tequila_params = {
            "fly_from": "LON",
            "fly_to": iata_code,
            "date_from": current_date,
            "date_to": latest_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0,
            "one_for_city": 1,
        }

        response = requests.get(url=tequila_endpoint, params=tequila_params, headers=self.tequila_headers)
        response.raise_for_status()
        flight_data = response.json()["data"]
        return FlightData(flight_data)
