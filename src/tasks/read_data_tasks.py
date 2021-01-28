from prefect.core import Task
from dask import dataframe as dd
import pandas as pd


class DataReader(Task):
    def __init__(self):
        super().__init__()

    def _read_dask(self):
        df = pd.read_csv('spy.csv')
        return dd.from_pandas(df, npartitions=3)

    def _read_pandas(self):
        pass

    def run(self, data_type):
        if data_type == 'dask':
            return self._read_dask()
        if data_type == 'pandas':
            raise NotImplementedError
