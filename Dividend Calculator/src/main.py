from src import TiingoQuotes
import datetime
from src import graphing


def main():
    # valid_columns form Tiingo api {'open', 'high', 'low', 'close', 'volume', 'adjOpen', 'adjHigh', 'adjLow',
    #                  'adjClose', 'adjVolume', 'divCash', 'splitFactor'}

    # Dataframe columns as of 12/15/2020(['close', 'high', 'low', 'open', 'volume', 'adjClose', 'adjHigh',
    #        'adjLow', 'adjOpen', 'adjVolume', 'divCash', 'splitFactor', 'date',
    #        'assets', 'shares']

    symbol = "PEP"
    end = datetime.datetime.today().strftime("%Y-%m-%d")
    data1 = TiingoQuotes.DividendCalculator(
        symbol, initial_price=1000, end=end, start="2000-02-07"
    )
    graphing.graphing(data1=data1)


if __name__ == "__main__":
    main()
