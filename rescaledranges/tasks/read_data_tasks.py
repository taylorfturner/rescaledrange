from prefect.core import Task
from dask import dataframe as dd
import pandas as pd


class DataReader(Task):
    def __init__(self):
        """
        DataReader Subclass of Prefect Task class.

        :Example:
        >>> data_reader = DataReader()
        >>> data_reader
        >>> <Task: DataReader>
        >>> data_reader.run()
        """
        super().__init__()

    def _read_dask(self, ticker):
        """[summary]

        :param ticker: [description]
        :type ticker: [type]
        :return: [description]
        :rtype: [type]
        """
        df = pd.read_csv(f'data/{ticker}.csv')
        return dd.from_pandas(df, npartitions=3)

    def _read_pandas(self, ticker):
        """[summary]

        :param ticker: [description]
        :type ticker: [type]
        :return: [description]
        :rtype: [type]
        """
        return pd.read_csv(f'data/{ticker}.csv')

    def run(self, data_type, ticker):
        """[summary]

        :param data_type: [description]
        :type data_type: [type]
        :param ticker: [description]
        :type ticker: [type]
        :raises ValueError: [description]
        :return: [description]
        :rtype: [type]
        """
        if data_type == 'dask':
            return self._read_dask(ticker)
        elif data_type == 'pandas':
            return self._read_pandas(ticker)
        else:
            raise ValueError("Only Dask or Pandas accepted")
