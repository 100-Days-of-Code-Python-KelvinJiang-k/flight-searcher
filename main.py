from flight_search import FlightSearch
from data_manager import DataManager

flight_searcher = FlightSearch()
data_manager = DataManager()

# sheety_response = requests.get("https://api.sheety.co/954119ebc378bd2f70a8a60b57fdd0d2/flightDeals/prices")
# sheet_data = sheety_response.json()["prices"]
sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]


def update_IATA_codes():
    for city in sheet_data:
        if city['iataCode'] == '':
            city['iataCode'] = flight_searcher.get_IATA_code(city['city'])
    data_manager.update_sheet(sheet_data)


for city in sheet_data:
    flight = flight_searcher.find_flight(city['iataCode'])
    if city['lowestPrice'] > flight.price:
        print(flight.price)

