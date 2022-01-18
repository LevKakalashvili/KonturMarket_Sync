"""В модуле описаны классы для работы с сервисом Контур.Маркет https://market.kontur.ru/"""

from dataclasses import dataclass
from typing import Any

from bs4 import BeautifulSoup
import requests

import konturmarket_urls as km_urls
import privatedata.kontrurmarket_privatedata as km_pvdata

session = requests.Session()

@dataclass
class GoodEGAIS:
    """Класc описывает структуру товара, продукции в соответствии с терминами ЕГАИС"""
    name: str = ''  # ЕГАИС наименование
    # Код алкогольной продукции (код АП) в ЕГАИС. Уникальный 19-ти значный код. Если значящих цифр в
    # коде меньше 19-ти, то в перед дописываются нули. Это при строковом представлении
    ap_code: int = 0

    def get_ap_code(self) -> str:
        """Метод возвращает строковое 19-ти символьное представление кода алкогольной продукции"""
        return self.ap_code.__str__()


@dataclass()
class KonturMarket:
    """Класс описывает работу с сервисом Контур.Маркет https://market.kontur.ru/"""

    def login(self) -> bool:
        auth_data = {
            'Login': km_pvdata.USER,
            'Password': km_pvdata.PASSWORD,
            'Remember': 'false'
        }
        try:
            # Пытаемся залогинится на сайте
            response = session.post(
                url=km_urls.get_url(km_urls.UrlType.login),
                data=auth_data,
                headers=km_urls.get_headers()
            )
            response.raise_for_status()
        except requests.RequestException as error:
            return False  # возвращаем False есди не удалось авторизоваться
        return True

    def get_goods_egais_name(self):
        try:
            response = session.get(
                url=km_urls.get_url(km_urls.UrlType.egais_name),
                headers=km_urls.get_headers()
            )
            response.raise_for_status()
            print(response.text)
        except requests.RequestException as error:
            return 0