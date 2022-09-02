class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, data):
        if not data:
            self.flight_exist = False
        else:
            self.flight_exist = True
            flight_data = data[0]
            self.data = flight_data
            self.city_from = flight_data['cityFrom']
            self.city_code_from = flight_data['cityCodeFrom']
            self.city_to = flight_data['cityTo']
            self.city_code_to = flight_data['cityCodeTo']
            self.price = flight_data['price']
            self.departure_date = flight_data['route'][0]['utc_departure']
            self.return_date = flight_data['route'][1]['utc_departure']
