import requests


# Определи класс для Яндекс Карт
class YaMapsClient:
    api_url = 'https://geocode-maps.yandex.ru/1.x/'

    def __init__(self):
        self.api_key = '46651a90-ff2c-43d4-85ec-ca631bdbc8a0'

    def request(self, data: str):
        r = requests.get(self.api_url,  # Ссылка для запроса к API Яндекс Карт
                         params=dict(format='json',  # Хотим получать файл в JSON-формате
                                     apikey=self.api_key,  # Наш ключ
                                     geocode=data))  # Адрес или координаты
        # Обрабатываем статус ответа. Если всё в порядке, возвращаем ответ
        if r.status_code == 200:
            return r.json()['response']
        elif r.status_code == 403:
            raise Exception('Такого адреса|координат нет')
        else:
            raise Exception('Что-то пошло не так, но не из-за адреса')

    def get_coords_by_address(self, address: str):
        '''
        Получение координат для адреса
        '''
        # Применяем нашу функцию отправки запроса и достаём из полученного словаря
        # нужную информацию по ключам
        coords = self.request(address)['GeoObjectCollection']['featureMember']

        # Если ответ пустой, то «поднимаем» ошибку
        if not coords:
            raise Exception('Пустой ответ')

        # Далее разделяем ответ в виде строки на две координаты и преобразуем их к числам
        coords = coords[0]['GeoObject']['Point']['pos']
        lon, lat = coords.split(' ')
        return float(lon), float(lat)
