from src import TiingoQuotes
import matplotlib.pyplot as plt
import numpy as np
import datetime


def normalize_data(data):
    # normalize assets column for comparison to other dataframes
    return (data - data[0]) / (data[0]) * 100


def main():
    # valid_columns form Tiingo api {'open', 'high', 'low', 'close', 'volume', 'adjOpen', 'adjHigh', 'adjLow',
    #                  'adjClose', 'adjVolume', 'divCash', 'splitFactor'}

    # Dataframe columns as of 12/15/2020(['close', 'high', 'low', 'open', 'volume', 'adjClose', 'adjHigh',
    #        'adjLow', 'adjOpen', 'adjVolume', 'divCash', 'splitFactor', 'date',
    #        'assets', 'shares']

    symbol = 'AAPL'
    end = datetime.datetime.today().strftime('%Y-%m-%d')
    data1 = TiingoQuotes.DividendCalculator(symbol, initial_price=100000, end=end, start='2020-08-28')


    # graphing MACD & signal line
    # fig, ax = plt.subplots()
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Gain')
    # total_gain1 = normalize_data(data1['assets'])
    #
    # ax.plot(data1['date'], total_gain1, label="Gain", color ='b')
    # plt.show()
    data1.dataframe.plot()


if __name__ == '__main__':
    main()
