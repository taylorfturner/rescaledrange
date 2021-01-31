import pytest
from prefect import Task
from rescaledranges.tasks.read_data_tasks import DataReader

def test_data_reader_no_params():
    data_reader = DataReader()
    assert data_reader

def test_data_reader_failure_data_frame_type():
    with pytest.raises(ValueError):
        data_reader = DataReader()
        data_reader.run(
            data_frame_type='fail',
            data_type='csv',
            ticker='one')

def test_data_reader_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        data_reader = DataReader()
        data_reader.run(
            data_frame_type='pandas',
            data_type='csv',
            ticker='one')

def test_data_reader_type():
    data_reader = DataReader()
    assert type(data_reader) == type(Task)