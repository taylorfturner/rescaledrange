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

    def _read_dask(self, file_path):
        """[summary]

        :param file_path: [description]
        :type file_path: [type]
        :return: [description]
        :rtype: [type]
        """
        df = pd.read_csv(file_path)
        return dd.from_pandas(df, npartitions=3)

    def _read_pandas(self, file_path):
        """[summary]

        :param file_path: [description]
        :type file_path: [type]
        :return: [description]
        :rtype: [type]
        """
        return pd.read_csv('spy.csv')

    def run(self, data_type, file_path):
        """[summary]

        :param data_type: [description]
        :type data_type: [type]
        :param file_path: [description]
        :type file_path: [type]
        :raises self._read_pandas: [description]
        :raises ValueError: [description]
        :return: [description]
        :rtype: [type]
        """
        if data_type == 'dask':
            return self._read_dask(file_path)
        elif data_type == 'pandas':
            raise self._read_pandas(file_path)
        else: 
            raise ValueError
