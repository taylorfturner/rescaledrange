from prefect.core import Task
from dask import dataframe as dd
import pandas as pd
import yfinance as yf


class DataReader(Task):
    def __init__(
        self,
        config={
            "data_frame_type": "pandas",
            "data_type": "csv",
            "data_location": "local"
        },
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
        self.data_frame_type = config.get("data_frame_type", "pandas")
        self.data_type = config.get("data_type", "csv")
        self.data_location = config.get("data_location", "local")
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

    def _query_yahoo(self, ticker):
        """[summary]

        :param ticker: [description]
        :type ticker: [type]
        :param data_type: [description]
        :type data_type: [type]
        """
        try:
            df = yf.download(ticker, start="2000-01-01", end="2021-02-16")

            # TODO: fix for 1 ticker: receives a too many values to unpack error
            df.columns = ["%s%s" % (a, "|%s" % b if b else "") for a, b in df.columns]
            df = df.reset_index()

            df["year"] = pd.to_datetime(df["Date"]).dt.year
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
        :return: [description]
        :rtype: [type]
        """
        if self.data_location == "local":
            return self._read_local(ticker)
        elif self.data_location == "yahoo":
            return self._query_yahoo(ticker)
        else:
            raise ValueError("Only local or yahoo accepted as data location")
