from functions.withdraw import withdraw_binance
from functions.balance import balance_btc

def main():
    balance_btc()
    withdraw_binance()

if __name__ == '__main__':
    main()

"""
Когда один модуль зависит от другого, а тот, в свою очередь, 
пытается обратиться обратно к первому то возникает циклический импорт,
Python не может завершить процесс загрузки, так как 
оба модуля ждут завершения друг друга. Это создает замкнутую цепочку, 
которая мешает программе корректно работать.
"""