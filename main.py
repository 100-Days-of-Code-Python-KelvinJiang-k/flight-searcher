from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flight_searcher = FlightSearch()
data_manager = DataManager()
notif_manager = NotificationManager()

sheet_data = data_manager.get_prices_sheet()


def update_IATA_codes():
    for row in sheet_data:
        if row['iataCode'] == '':
            row['iataCode'] = flight_searcher.get_IATA_code(row['city'])
    data_manager.update_prices_sheet(sheet_data)


def get_cheapest_flights():
    for city in sheet_data:
        flight = flight_searcher.find_flight(city['iataCode'])

        if not flight.flight_exist:
            continue
        elif city['lowestPrice'] > flight.price:
            flight_link = f"https://www.google.co.uk/flights?hl=en#flt={flight.city_code_from}" \
                          f".{flight.city_code_to}.{flight.departure_date}*{flight.city_code_to}" \
                          f".{flight.city_code_from}.{flight.return_date}"
            message = f"Subject: Low price alert!\n\n" \
                      f"Only £{flight.price} to fly from {flight.city_from}-{flight.city_code_from} " \
                      f"to {flight.city_to}-{flight.city_code_to}, from {flight.departure_date} to {flight.return_date}." \
                      f"\nFlight has {flight.stop_overs} stop over, via departure cities {flight.via_to_city} and" \
                      f"return cities {flight.via_from_city}\n{flight_link}"
            notif_manager.send_email_to_all(message=message)


def register_user():
    first_name = input("First Name? ")
    last_name = input("Last Name? ")
    email = input("Email? ")
    user_config = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }
    data_manager.add_user(user_config)


get_cheapest_flights()
