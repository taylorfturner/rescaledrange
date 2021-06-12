from prefect.core import Task
from dask import dataframe as dd
import pandas as pd
import yfinance as yf


class DataReader(Task):
    def __init__(
        self,
        data_frame_type="pandas",
        data_type="csv",
        data_location="local",
        config={"start": '2000-01-01', "end": "2021-02-17"}
    ):
        """
        DataReader Subclass of Prefect Task class for reading
        either Locally (Dask or Pandas) or query from Yahoo finance.

        :Example:
        >>> data_reader = DataReader()
        >>> data_reader
        <Task: DataReader>
        >>> data_reader.run()
        """
        self.data_frame_type = data_frame_type
        self.data_type = data_type
        self.data_location = data_location
        self.config = config
        super().__init__()

    def _read_dask(self, ticker):
        """Hidden method to read data as dask dataframe

        :param ticker: [description]
        :type ticker: [type]
        :return: [description]
        :rtype: [type]
        """
        df = pd.read_csv(f"data/{ticker}.{self.data_type}")
        return dd.from_pandas(df, npartitions=3)

    def _read_pandas(self, ticker):
        """Hidden method to read data as pandas dataframe

        :param ticker: [description]
        :type ticker: [type]
        :return: [description]
        :rtype: [type]
        """
        return pd.read_csv(f"data/{ticker}.{self.data_type}")


    def _query_yahoo(self, ticker, config):
        """Hidden method to query the Yahoo API and return
        pandas dataframe
        
        :param ticker: [description]
        :type ticker: [type]
        :param data_type: [description]
        :type data_type: [type]
        """
        df = yf.download(ticker,interval="1d", **config)
        df = df.reset_index()

        return df


    def _read_local(self, ticker):
        """Hidden method to read data from localhost

        :param ticker: [description]
        :type ticker: [type]
        :return: [description]
        :rtype: [type]
        """
        if self.data_frame_type == "dask":
            return self._read_dask(ticker)
        elif self.data_frame_type == "pandas":
            return self._read_pandas(ticker)
        else:
            raise ValueError("Only dask or pandas accepted as data_frame_type")

    def run(self, ticker):
        """Primary run method required due
        to prefect task class inheritance.

        :param ticker: Time series ticker or ID
        :type ticker: str, required
        :raises ValueError: Only localhost or yahoo allowed at this time
        :return: either a pandas dataframe or a string that is the valueerror
        :rtype: ValueError
        """
        if self.data_location == "local":
            return self._read_local(ticker)
        elif self.data_location == "yahoo":
            return self._query_yahoo(ticker, config=self.config)
        else:
            raise ValueError("Only local or yahoo accepted as data location")
