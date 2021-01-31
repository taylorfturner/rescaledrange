import pytest 
import pandas as pd

@pytest.fixture('data_fixture')
def read_data(data_type, ticker):
    return pd.DataFrame('../../rescaledranges/data/{ticker}.{data_type}')
