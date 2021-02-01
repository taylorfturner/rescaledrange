import pytest
from prefect import Task, Flow
from rescaledranges.tasks.read_data_tasks import DataReader

@pytest.fixture
def flow():
    return Flow('test_read_data_flow')

def test_data_reader_no_params(flow):
    data_reader = DataReader()
    flow.add_task(data_reader)
    assert data_reader in flow.tasks
    assert len(flow.tasks) == 1

def test_data_reader_failure_data_frame_type():
    with pytest.raises(ValueError):
        data_reader = DataReader()
        data_reader.run(
            data_frame_type='fail',
            data_type='csv',
            ticker='one')

def test_data_reader_pandas_run():
    with pytest.raises(FileNotFoundError):
        data_reader = DataReader()
        data_reader.run(
            data_frame_type='pandas',
            data_type='csv',
            ticker='one')

def test_data_reader_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        data_reader = DataReader()
        data_reader.run(
            data_frame_type='dask',
            data_type='csv',
            ticker='one')
