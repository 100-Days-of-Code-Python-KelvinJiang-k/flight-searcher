import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def update_sheet(self, sheet):
        for row in sheet:
            sheety_endpoint = f"https://api.sheety.co/954119ebc378bd2f70a8a60b57fdd0d2/flightDeals/prices/{row['id']}"
            sheety_params = {
                "price": row
            }
            response = requests.put(url=sheety_endpoint, json=sheety_params)
            response.raise_for_status()
