import pandas
from tiingo import TiingoClient
import datetime as date_time
from src.settings import client

# access api key from settings.py file
# before adding to github, add .env to .gitignore files


class Quotes:
    def __init__(self, ticker, metric_name=None):
        # if tickers are list value, metric_name is needed to return 1 tiingo data point
        self.ticker = ticker
        file = open("supported_tickers.csv", "r")
        valid_tickers = file.read()

        # validates tickers (case sensistive).
        if type(self.ticker) is str:
            if self.ticker not in valid_tickers:
                raise RuntimeError("{} is not found in Tiingo's database.".format({}))

        elif type(self.ticker) is list:
            valid_list = []
            for symbol in self.ticker:
                if symbol in valid_tickers:
                    valid_list.append(symbol)

            self.ticker = valid_list

            if len(self.ticker) == 0:
                raise RuntimeError("No valid ticker(s).")
            elif len(self.ticker) == 1:
                self.ticker = self.ticker[0]

        self.client = client
        self.current_day_datetime = date_time.datetime.today()
        self.current_day_string = self.current_day_datetime.strftime(r'%m/%d/%Y')

        self.start_datetime = self.current_day_datetime - date_time.timedelta(days=365)
        self.start_string = self.start_datetime.strftime(r'%m/%d/%Y')

        self.dataframe = client.get_dataframe(tickers=self.ticker, metric_name=metric_name, startDate=self.start_string,
                                              endDate=self.current_day_string)
        file.close()











