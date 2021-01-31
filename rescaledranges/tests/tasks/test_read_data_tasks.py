import pytest
from rescaledranges.tasks.read_data_tasks import DataReader


def test_data_reader_no_params():
    assert DataReader()
