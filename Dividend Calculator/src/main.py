from src import TiingoQuotes
import matplotlib.pyplot as plt


def moving_average(data, months: int):
    # X month ma with -365 start date from today
    # used temp label (XXX) to be replaced later
    data['XXX'] = data['close'].rolling(months, min_periods=months).mean()


def exp_moving_average(data, months: int):
    # X month ma with -365 start date from today
    # used temp label (XXX) to be replaced later
    data['XXX'] = data['close'].ewm(min_periods=0, span=months, adjust=False).mean()


def macd(data):
    exp_moving_average(data, 12)
    data['12exp_ma'] = data.pop('XXX')
    exp_moving_average(data, 26)
    data['26exp_ma'] = data.pop('XXX')

    data['MACD'] = data['12exp_ma'] - data['26exp_ma']
    data.pop('12exp_ma')
    data.pop('26exp_ma')

    exp_moving_average(data, 9)
    data['Signal'] = data.pop('XXX')


def main():
    # for valid columns from tiingo dataframe.valid_columns
    symbol = ['AMD']
    data = TiingoQuotes.Quotes(symbol).dataframe
    exp_moving_average(data, 12)

    print(data['MACD'].tail(50))


if __name__ == '__main__':
    main()
