import datetime
from src.settings import client
import math


class Quotes:
    def __init__(self, ticker, start_date=None, end_date=None, metric_name=None):
        # isoformat for date yyyy-mm-dd
        if start_date is None:
            self.start_date = self.current_day_date - datetime.timedelta(days=365)
        else:
            self.start_date = datetime.date.fromisoformat(start_date)

        if end_date is None:
            self.current_day_date = datetime.date.today()
        else:
            self.end_date = datetime.date.fromisoformat(end_date)

        self.ticker = Quotes.validate_ticker(ticker)
        self.start_string = self.start_date.strftime(r'%m/%d/%Y')
        self.current_day_string = self.current_day_date.strftime(r'%m/%d/%Y')

        # if tickers is list value, metric_name is needed to return a tiingo data point
        self.dataframe = client.get_dataframe(tickers=self.ticker, metric_name=metric_name, startDate=self.start_string,
                                              endDate=self.current_day_string)
        # adding the dates as the x index for dataframe
        reference_dates = list()
        for date in self.dataframe.index.date:
            date = date.strftime(r'%m/%d/%Y')
            reference_dates.append(date)
        self.dataframe['date'] = reference_dates
        self.dataframe.set_index(keys='date', inplace=True)

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


class DividendCalculator(Quotes):
    def __init__(self, ticker, initial_price, start=None, end_date=None):
        super().__init__(ticker, start_date=start, metric_name=None)

        '''
            Dividend Calculator
            Need start date, end date, and ticker information, and initial $$$
            calculate graph of the info, annual return rate, and number of shares initial and final

        '''
        self.initial_shares = math.floor(initial_price/self.dataframe['adjClose'][0])
        self.shares = self.initial_shares
        self.initial_equity = self.initial_shares * self.dataframe['adjClose'][0]
        self.total_dividends, new_dividend = 0, 0
        index = 0

        for dividend_per_share in self.dataframe['divCash']:

            if dividend_per_share != 0:
                new_dividend = self.shares * dividend_per_share

                # drip reinvestment
                self.shares += new_dividend / self.dataframe['adjClose'][index]
                self.total_dividends += new_dividend

            index += 1


class Calculations:
    @staticmethod
    def moving_average(data, months: int):
        # X month ma with -365 start date from today
        # used temp label (XXX) to be replaced later
        data['XXX'] = data['adjClose'].rolling(months, min_periods=months).mean()

    @staticmethod
    def exp_moving_average(data, months: int):
        # X month ma with -365 start date from today
        # used temp label (XXX) to be replaced later
        data['XXX'] = data['adjClose'].ewm(min_periods=0, span=months, adjust=False).mean()

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




