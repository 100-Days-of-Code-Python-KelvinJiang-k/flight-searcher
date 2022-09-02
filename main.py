from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flight_searcher = FlightSearch()
data_manager = DataManager()
notif_manager = NotificationManager()

sheet_data = data_manager.get_sheet()
# sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 26000, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]


def update_IATA_codes():
    for row in sheet_data:
        if row['iataCode'] == '':
            row['iataCode'] = flight_searcher.get_IATA_code(row['city'])
    data_manager.update_sheet(sheet_data)


for city in sheet_data:
    flight = flight_searcher.find_flight(city['iataCode'])
    if flight.flight_exist and city['lowestPrice'] > flight.price:
        message = f"Subject: Low price alert!\n\n" \
                  f"Only £{flight.price} to fly from {flight.city_from}-{flight.city_code_from} " \
                  f"to {flight.city_to}-{flight.city_code_to}, from {flight.departure_date} to {flight.return_date}."
        notif_manager.send_email(message=message)

