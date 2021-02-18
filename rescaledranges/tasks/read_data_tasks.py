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
        >>> <Task: DataReader>
        >>> data_reader.run()
        """
        self.data_frame_type = data_frame_type
        self.data_type = data_type
        self.data_location = data_location
        self.config = config
        super().__init__()

    def _read_dask(self, ticker):
        """[summary]

        :param ticker: [description]
        :type ticker: [type]
        :return: [description]
        :rtype: [type]
        """
        try:
            df = pd.read_csv(f"data/{ticker}.{self.data_type}")
            return dd.from_pandas(df, npartitions=3)
        except Exception as e:
            raise e

    def _read_pandas(self, ticker):
        """[summary]

        :param ticker: [description]
        :type ticker: [type]
        :return: [description]
        :rtype: [type]
        """
        try:
            return pd.read_csv(f"data/{ticker}.{self.data_type}")
        except Exception as e:
            raise e

    def _query_yahoo(self, ticker, config):
        """[summary]

        :param ticker: [description]
        :type ticker: [type]
        :param data_type: [description]
        :type data_type: [type]
        """
        try:
            df = yf.download(ticker,interval="1mo", **config)
            df = df.reset_index()

            return df

        except Exception as e:
            raise e

    def _read_local(self, ticker):
        """[summary]

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
        """[summary]

        :param ticker: [description]
        :type ticker: [type]
        :raises ValueError: [description]
        :return: [description]s
        :rtype: [type]
        """
        if self.data_location == "local":
            return self._read_local(ticker)
        elif self.data_location == "yahoo":
            return self._query_yahoo(ticker, config=self.config)
        else:
            raise ValueError("Only local or yahoo accepted as data location")
