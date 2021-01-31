import pytest
from prefect import Task
from rescaledranges.tasks.read_data_tasks import DataReader


def test_data_reader_no_params():
    assert DataReader()

def test_data_reader_type():
    data_reader = DataReader()
    assert type(data_reader) == type(Task)
