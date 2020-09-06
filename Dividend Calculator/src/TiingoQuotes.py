import datetime as date_time
from src.settings import client


class Quotes:
    def __init__(self, ticker, start_date=None, metric_name=None):
        self.ticker = Quotes.validate_ticker(ticker)
        self.client = client
        self.current_day_date = date_time.date.today()
        self.current_day_string = self.current_day_date.strftime(r'%m/%d/%Y')

        if start_date is None:
            self.start_datetime = self.current_day_date - date_time.timedelta(days=365)
        else:
            self.start_datetime = date_time.date.fromisoformat(start_date)

        self.start_string = self.start_datetime.strftime(r'%m/%d/%Y')

        # if tickers are list value, metric_name is needed to return 1 tiingo data point
        self.dataframe = client.get_dataframe(tickers=self.ticker, metric_name=metric_name, startDate=self.start_string,
                                              endDate=self.current_day_string)
        self.dataframe['date'] = self.dataframe.index.date

    @staticmethod
    def validate_ticker(ticker):
        file = open("supported_tickers.csv", "r")
        valid_tickers = file.read()

        # validates tickers (case sensistive).
        if type(ticker) is str:
            if ticker not in valid_tickers:
                raise RuntimeError("{} is not found in Tiingo's database.".format({}))

        elif type(ticker) is list:
            valid_list = []
            for symbol in ticker:
                if symbol in valid_tickers:
                    valid_list.append(symbol)

            ticker = valid_list

            if len(ticker) == 0:
                raise RuntimeError("No valid ticker(s).")
            elif len(ticker) == 1:
                ticker = ticker[0]

        file.close()

        return ticker


class Calculations:
    @staticmethod
    def moving_average(data, months: int):
        # X month ma with -365 start date from today
        # used temp label (XXX) to be replaced later
        data['XXX'] = data['close'].rolling(months, min_periods=months).mean()

    @staticmethod
    def exp_moving_average(data, months: int):
        # X month ma with -365 start date from today
        # used temp label (XXX) to be replaced later
        data['XXX'] = data['close'].ewm(min_periods=0, span=months, adjust=False).mean()

    @staticmethod
    def macd(data):
        Calculations.exp_moving_average(data, 12)
        data['12exp_ma'] = data.pop('XXX')
        Calculations.exp_moving_average(data, 26)
        data['26exp_ma'] = data.pop('XXX')

        data['MACD'] = data['12exp_ma'] - data['26exp_ma']
        data.pop('12exp_ma')
        data.pop('26exp_ma')

        data['Signal'] = data['MACD'].ewm(min_periods=0, span=9, adjust=False).mean()
        data['delta'] = data['MACD'] - data['Signal']



