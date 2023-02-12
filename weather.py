class Geocoder:
    def __init__(self, api_key: str, city: str) -> None:
        self.api_key = api_key
        self.city = city

    def get_coordinates(self) -> tuple:
        pass


class Weather:
    def __init__(self, api_key: str, city: str):
        city_geo = Geocoder(api_key, city)
        coordinates = city_geo.get_coordinates()
        self.lat = coordinates[0]
        self.lon = coordinates[1]

    def forecast_12h(self):
        pass

    def forecast_12h_simplified(self):
        pass
