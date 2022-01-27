"""Модуль для запуска синхронизации Контур.Маркета с БД"""
from konturmarket_class_lib import KonturMarket


if __name__ == "__main__":
    kmarket = KonturMarket()
    if kmarket.login():
        kmarket.get_egais_assortment()
        print(1)