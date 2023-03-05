import requests
import json
from api_key import api_key


class Geolocator:
    def __init__(self, api_k: str, city: str) -> None:
        self.api_k = api_k
        self.city = city

    def get_coordinates(self) -> tuple:
        response = json.loads(self._get_response())
        if response:
            return response[0]['lat'], response[0]['lon']
        return None, None

    def _get_response(self):
        base_url = 'https://api.openweathermap.org/geo/1.0/direct'
        r = requests.get(f'{base_url}?q={self.city}&limit=1&appid='
                         f'{self.api_k}&units=metric')
        return r.content


class Weather:
    def __init__(self, api_k: str, city: str = None, lat=None, lon=None) -> None:
        self.api_k = api_k
        if city:
            self.lat, self.lon = Geolocator(self.api_k, city).get_coordinates()
            self.data = json.loads(self._get_response())
        elif lat and lon:
            self.lat = lat
            self.lon = lon
            self.data = json.loads(self._get_response())

    def _get_response(self):
        base_url = 'https://api.openweathermap.org/data/2.5/forecast'
        r = requests.get(f'{base_url}?lat={self.lat}&lon={self.lon}&'
                         f'appid={self.api_k}&units=metric')
        return r.text

    def forecast_12h(self) -> str:
        try:
            data = str(self.data['list'][:4])
        except (AttributeError, KeyError):
            data = 'There are no such coordinates. Provide another city ' \
                   'or a lat and lon arguments'
        return data

    def forecast_12h_simplified(self):
        simple_data = list()
        try:
            data = self.data['list'][:4]
            for period in data:
                simple_data.append(
                    (
                        period['dt_txt'],
                        period['main']['temp'],
                        period['weather'][0]['description']
                    )
                )
        except (AttributeError, KeyError):
            simple_data = 'There are no such coordinates. Provide another city ' \
                          'or a lat and lon arguments'
        return simple_data


if __name__ == '__main__':
    weather = Weather(api_key, city='Haifa')
    print(weather.forecast_12h_simplified())
