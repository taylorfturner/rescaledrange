from prefect.core import Task
from dask import dataframe as dd
import pandas as pd


class DataReader(Task):
    def __init__(self):
        """
        DataReader Subclass of Prefect Task class.

        :Example:
        >>> data_reader = DataReader()
        >>> data_reader.run()
        """
        super().__init__()

    def _read_dask(self, ticker):
        df = pd.read_csv(f'data/{ticker}.csv')
        return dd.from_pandas(df, npartitions=3)

    def _read_pandas(self, ticker):
        return pd.read_csv(f'data/{ticker}.csv')

    def run(self, data_type, ticker):
        if data_type == 'dask':
            return self._read_dask(ticker)
        elif data_type == 'pandas':
            return self._read_pandas(ticker)
        else:
            raise ValueError
