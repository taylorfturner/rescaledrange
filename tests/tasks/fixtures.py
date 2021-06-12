import pytest 
import pandas as pd
from prefect import Flow

@pytest.fixture
def fixture_flow():
    return Flow('test_read_data_flow')

@pytest.fixture
def iwm_test_data():
    return pd.read_csv('rescaledranges/data/IWM.csv')
