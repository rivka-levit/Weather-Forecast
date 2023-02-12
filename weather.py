import requests
import json
from api_key import api_key


class Geolocator:
    def __init__(self, api_k: str, city: str) -> None:
        self.api_key = api_k
        self.city = city

    def get_coordinates(self) -> tuple:
        response = json.loads(self._get_response())
        return response[0]['lat'], response[0]['lon']

    def _get_response(self):
        base_url = 'http://api.openweathermap.org/geo/1.0/direct'
        r = requests.get(f'{base_url}?q={self.city}&limit=1&appid='
                         f'{self.api_key}&units=metric')
        return r.content


class Weather:
    def __init__(self, api_k: str, city: str):
        city_geo = Geolocator(api_k, city)
        coordinates = city_geo.get_coordinates()
        self.lat = coordinates[0]
        self.lon = coordinates[1]

    def forecast_12h(self):
        pass

    def forecast_12h_simplified(self):
        pass


if __name__ == '__main__':
    g = Geolocator(api_key, 'London')
    print(g.get_coordinates())
