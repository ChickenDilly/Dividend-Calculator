import datetime
from src import TiingoQuotes
from src.TiingoQuotes import Calculations as calc
import matplotlib.pyplot as plt
import numpy as np


def main():
    # for valid columns from tiingo check dataframe.valid_columns
    symbol = ['AMD']
    data = TiingoQuotes.Quotes(symbol).dataframe
    calc.macd(data)

    # graphing MACD & signal line
    '''
    fig, ax = plt.subplots()
    ax.plot(data['date'], data['MACD'], label='MACD')
    ax.plot(data['date'], data['Signal'], label='Signal Line')
    ax.set_xlabel('Date')
    plt.show()
    '''



if __name__ == '__main__':
    main()
