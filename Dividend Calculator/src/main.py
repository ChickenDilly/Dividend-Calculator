import datetime
from src import TiingoQuotes
import matplotlib.pyplot as plt
import numpy as np


def main():
    # for valid columns from tiingo check dataframe.valid_columns
    symbol = 'KO'
    start_date = '1999-01-01'
    data = TiingoQuotes.DividendCalculator(symbol, initial_price=1000, start=start_date)
    print(data.total_dividends)

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
