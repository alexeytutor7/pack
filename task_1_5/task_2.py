from functions.withdraw import (
    withdraw_binance as bin,
    withdraw_kucoin as ku,
    withdraw_okx as okx,
    withdraw_huobi as hu,
    withdraw_bybit as byb,
    withdraw_kraken as kra,
    withdraw_gateio as gate,
    withdraw_bitfinex as bitf,
)

def main():
    bin()
    ku()
    okx()
    hu()
    byb()
    kra()
    gate()
    bitf()

if __name__ == '__main__':
    main()
