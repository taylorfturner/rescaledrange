import pytest 
import pandas as pd

@pytest.fixture('data_fixture')
def data_fixture():
    return pd.DataFrame('../../rescaledranges/data/{}.{}')
