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
            self.departure_date = flight_data['route'][0]['utc_departure'].split("T")[0]
            self.return_date = flight_data['route'][1]['utc_departure'].split("T")[0]
            self.stop_overs = (len(flight_data['route']) - 2) // 2
            self.via_city = []
            # TODO: Specifically determine which cities are stopover to, from cities by checking when destination is met

            # Obtains a list of all stopover cities, including those on the return trip
            for city in flight_data['route']:
                if city['cityFrom'] not in ([self.city_from, self.city_to] + self.via_city):
                    self.via_city.append(city['cityFrom'])
            self.via_to_city = self.via_city[0:len(self.via_city) // 2]
            self.via_from_city = self.via_city[len(self.via_city) // 2:len(self.via_city)]
