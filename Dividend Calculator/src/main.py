import datetime
from src import TiingoQuotes
import matplotlib.pyplot as plt


def main():
    # for valid columns from tiingo check dataframe.valid_columns
    symbol = 'MSFT'
    end = '2020-09-14'
    data = TiingoQuotes.DividendCalculator(symbol, initial_price=1000, end=end)

    # graphing MACD & signal line

    fig, ax = plt.subplots()
    ax.plot(data.dataframe['date'], data.dataframe['adjClose'], label="Close")
    ax.plot(data.dataframe['date'], data.dataframe['total gain'], label="Gain")
    ax.set_xlabel('Date')
    plt.show()


if __name__ == '__main__':
    main()
