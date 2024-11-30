from functions import balance_btc, BTC_transfer, withdraw_binance


def main():
    balance_btc()
    BTC_transfer()
    withdraw_binance()


if __name__ == '__main__':
    main()

"""
Файл __init__.py — он указывает Python, что папка является пакетом, 
позволяет объединить несколько модулей в один пакет. 
В этом файле можно указать, какие функции или классы из разных модулей пакета будут доступны для использования.
"""
