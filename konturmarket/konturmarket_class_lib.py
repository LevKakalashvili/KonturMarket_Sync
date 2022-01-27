"""В модуле описаны классы для работы с сервисом Контур.Маркет https://market.kontur.ru/"""
import json
from dataclasses import dataclass
from typing import Any

import requests

from konturmarket_urls import Url, UrlType, get_url
import privatedata.kontrurmarket_privatedata as km_pvdata

session = requests.Session()

@dataclass
class GoodEGAIS:
    """Класc описывает структуру товара, продукции в соответствии с терминами ЕГАИС"""
    name: str = ''  # ЕГАИС наименование
    # Код алкогольной продукции (код АП) в ЕГАИС. Уникальный 19-ти значный код. Если значящих цифр в
    # коде меньше 19-ти, то в перед дописываются нули. Это при строковом представлении
    alco_code: int = 0

    def get_string_alco_code(self) -> str:
        """Метод возвращает строковое 19-ти символьное представление кода алкогольной продукции"""
        lenght = len(str(self.alco_code))
        return f'{str(0) * (19 - lenght)}{str(self.alco_code)}'

    def to_tuple(self):
        return (self.get_string_alco_code(), self.name)

@dataclass()
class KonturMarket:
    """Класс описывает работу с сервисом Контур.Маркет https://market.kontur.ru/"""

    def login(self) -> bool:
        auth_data = {
            'Login': km_pvdata.USER,
            'Password': km_pvdata.PASSWORD,
            'Remember': False
        }
        # auth_data = '{"Login":"kakalashvililev@yandex.ru","Password":"340354Lev!","Remember":false}'
        # Пытаемся залогиниться на сайте
        url: Url = get_url(UrlType.login)
        response = session.post(
            url=url.url,
            data=json.dumps(auth_data),
            headers=url.headers,
            cookies=url.cookies
        )
        return response.ok

    def get_egais_assortment(self):
        url: Url = get_url(UrlType.egais_assortment)
        response = session.get(url.url)
        goods = dict(response.json()).get('list')
        # Если в получили успешный ответ и есть список товаров
        if response.ok and goods:
            print(response.text)


if __name__ == "__main__":
    good = GoodEGAIS()
    good.name="Что-то"
    good.alco_code=123456789
    print(good.get_string_alco_code())