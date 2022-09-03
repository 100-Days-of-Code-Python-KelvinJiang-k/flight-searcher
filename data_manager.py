import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            "Authorization": os.environ.get("SHEETY_TOKEN"),
        }

    def get_prices_sheet(self):
        sheety_endpoint = "https://api.sheety.co/954119ebc378bd2f70a8a60b57fdd0d2/flightDeals/prices"
        sheety_response = requests.get(url=sheety_endpoint, headers=self.headers)
        sheety_response.raise_for_status()
        prices_sheet = sheety_response.json()["prices"]
        return prices_sheet

    def update_prices_sheet(self, sheet):
        for row in sheet:
            sheety_endpoint = f"https://api.sheety.co/954119ebc378bd2f70a8a60b57fdd0d2/flightDeals/prices/{row['id']}"
            sheety_params = {
                "price": row
            }
            sheety_response = requests.put(url=sheety_endpoint, json=sheety_params, headers=self.headers)
            sheety_response.raise_for_status()

    def get_users_sheet(self):
        sheety_endpoint = "https://api.sheety.co/954119ebc378bd2f70a8a60b57fdd0d2/flightDeals/users"
        sheety_response = requests.get(url=sheety_endpoint, headers=self.headers)
        sheety_response.raise_for_status()
        users_sheet = sheety_response.json()["users"]
        return users_sheet

    def add_user(self, user_info):
        sheety_endpoint = "https://api.sheety.co/954119ebc378bd2f70a8a60b57fdd0d2/flightDeals/users"
        sheety_response = requests.post(url=sheety_endpoint, json=user_info, headers=self.headers)
        sheety_response.raise_for_status()
