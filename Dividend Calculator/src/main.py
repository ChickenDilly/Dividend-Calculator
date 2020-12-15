from src import TiingoQuotes
import matplotlib.pyplot as plt
import datetime


def main():
    # for valid columns from tiingo check dataframe.valid_columns
    symbol = 'TSLA'
    end = datetime.datetime.today().strftime('%Y-%m-%d')
    data_1 = TiingoQuotes.DividendCalculator(symbol, initial_price=1000000, end=end, start='2020-08-28')
    data_1.dataframe.to_json('tsla.json')
    return

    data_2 = TiingoQuotes.DividendCalculator('MCD', initial_price=1000, end=end, start='2000-01-01')

    # graphing MACD & signal line

    fig, ax = plt.subplots()
    total_gain1 = (data_1.dataframe['total gain'] - data_1.dataframe['total gain'][0]) / (data_1.dataframe['total gain'][0]) * 100
    total_gain2 = (data_2.dataframe['total gain'] - data_2.dataframe['total gain'][0]) / (data_2.dataframe['total gain'][0]) * 100
    ax.set_xlabel('Date')

    ax.plot(data_1.dataframe['date'], total_gain1, label="Gain", color ='b')
    ax.plot(data_2.dataframe['date'], total_gain2, label="Gain", color='g')
    plt.show()


if __name__ == '__main__':
    main()
