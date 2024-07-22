
import requests
from pathlib import Path


class APIRequester():

    base_url = 'https://swapi.dev/'
    page = {'page': 1}

    def __init__(self, url=base_url):
        self.base_url = url

    def get(self, url=''):
        send_url = self.base_url + url
        try:
            response = requests.get(send_url, params=self.page)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException:
            print('Возникла ошибка при выполнении запроса')
            return False


class SWRequester(APIRequester):

    base_url = 'https://swapi.dev/api'

    def __init__(self, url=base_url):
        super().__init__(url)

    def get_sw_categories(self, url='/'):
        try:
            response = requests.get(self.base_url + url, params=self.page)
            response.raise_for_status()
            response = response.json()
            return response.keys()
        except requests.exceptions.RequestException:
            print('Ошибка при запросе категорий')
            return False

    def get_sw_info(self, sw_type, *args):
        url = f'{self.base_url}/{sw_type}/'
        for i in args:
            url += f'{i}/'
        response = requests.get(url, params=self.page)
        response.raise_for_status()
        return response.text


def save_sw_data():
    swapi = SWRequester('https://swapi.dev/api')
    Path('data').mkdir(exist_ok=True)
    for i in swapi.get_sw_categories():
        with open(f'data/{i}.txt', 'w+') as f:
            f.write(swapi.get_sw_info(i))


if __name__ == '__main__':
    save_sw_data()
