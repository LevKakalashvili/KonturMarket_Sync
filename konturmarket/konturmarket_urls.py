""" В модуле хранятся url'ы для сервиса Конутр.Маркет https://market.kontur.ru/."""
from enum import Enum
from typing import Any, Dict, NamedTuple

from fake_useragent import UserAgent

AUTH_URL = 'https://auth.kontur.ru/'
ASSORTMENT_EGAIS_URL = 'https://market.kontur.ru/a095a331-45ed-444e-8977-0a1eb28fee92/ae2fa6c7-dcbb-4c0b-b4e2-' \
                       '3d63bb6eabd5/055adf4b-e674-4dcd-9095-3e8c31785ac9#/goods/nomenclatureList/all?tabType=All'
# ASSORTMENT_EGAIS_URL = 'https://market.kontur.ru'

class UrlType(Enum):
    """Перечисление для определения, какой тип url необходимо сформировать.
    login - авторизация пользователя.
    egais_name - справочник товарв (ЕГАИС наименований)
    """

    login = 1
    egais_name = 2

class Url(NamedTuple):
    """Класс для описания url запроса в сервис Контур.Маркет."""

    url: str  # url для запроса в сервис

def get_headers() -> Dict[str, Any]:
    """Метод получения словаря заголовков для передачи в запросе к сервису МойСклад.
    :return:
        Если token пустой, то возвратится словарь для запроса token.
        Если не пустой возвратиться словарь для запросов сущностей МойСклад
    """
    headers = {
        'User-Agent': UserAgent().random
    }

    return headers

def get_url(url_type: UrlType) -> str:
    """Функция для получения url.
    :param url_type: UrlType.token - url для получения токена, UrlType.retail_demand - url для получения розничны
    продаж за определённый период
    :returns: Возвращается объект Url
    :rtypes: str
    """
    if url_type == UrlType.login:
        # Возвращаем ссылку на форму для авторизации в сервисе
        return AUTH_URL
    elif url_type == UrlType.egais_name:
        # Возвращаем ссылку на раздел в Товары/Пиво в сервисе Конутр.Маркет
        return ASSORTMENT_EGAIS_URL