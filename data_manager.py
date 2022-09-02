import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headings = os.environ.get("SHEETY_TOKEN")

    def get_sheet(self):
        sheety_response = requests.get("https://api.sheety.co/954119ebc378bd2f70a8a60b57fdd0d2/flightDeals/prices")
        sheet_data = sheety_response.json()["prices"]
        return sheet_data

    def update_sheet(self, sheet):
        for row in sheet:
            sheety_endpoint = f"https://api.sheety.co/954119ebc378bd2f70a8a60b57fdd0d2/flightDeals/prices/{row['id']}"
            sheety_params = {
                "price": row
            }
            response = requests.put(url=sheety_endpoint, json=sheety_params)
            response.raise_for_status()
