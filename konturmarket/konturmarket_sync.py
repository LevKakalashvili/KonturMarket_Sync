"""Модуль для запуска синхронизации Контур.Маркета с БД"""
from konturmarket_class_lib import KonturMarket


if __name__ == "__main__":
    km = KonturMarket()
    if km.login():
        km.get_goods_egais_name()
        print(1)