# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import MarketData


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(MarketData.Get_Option_Price('UVXY', 'call', 25, '2021-11-22')['Close'])
    print(MarketData.Get_Stock_Price('UVXY',start='2021-12-10')['Close'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
