class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        flight_data = data[0]
        self.price = flight_data['price']
        self.departure_date = flight_data['route'][0]['utc_departure']
        self.return_date = flight_data['route'][1]['utc_departure']

