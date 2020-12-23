from src import TiingoQuotes
import matplotlib.pyplot as plt
import datetime
from matplotlib.ticker import *


def normalize_data(data):
    # normalize dataframe column for comparison to other dataframes
    return (data - data[0]) / (data[0]) * 100


def main():
    # valid_columns form Tiingo api {'open', 'high', 'low', 'close', 'volume', 'adjOpen', 'adjHigh', 'adjLow',
    #                  'adjClose', 'adjVolume', 'divCash', 'splitFactor'}

    # Dataframe columns as of 12/15/2020(['close', 'high', 'low', 'open', 'volume', 'adjClose', 'adjHigh',
    #        'adjLow', 'adjOpen', 'adjVolume', 'divCash', 'splitFactor', 'date',
    #        'assets', 'shares']

    symbol = 'AAPL'
    end = datetime.datetime.today().strftime('%Y-%m-%d')
    data1 = TiingoQuotes.DividendCalculator(symbol, initial_price=10000, end=end, start='2018-08-28')

    # graphing MACD & signal line
    # setting up figure and legend
    fig, ax = plt.subplots()
    fig.autofmt_xdate(rotation=-65, ha='center', which='major')
    # setting up x/y axes and major/minor ticks
    ax.set_xlabel('Date'), ax.set_ylabel('Gain (%)')
    ax.xaxis.set_major_locator(MultipleLocator(30))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='major', width=2, length=8), ax.tick_params(which='minor', width=2, length=3)
    # data plotting
    total_gain1 = normalize_data(data1['assets'])
    ax.plot(data1['date'], total_gain1, label="Assets", color='b')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    main()
