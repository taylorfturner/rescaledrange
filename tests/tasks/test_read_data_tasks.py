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
    assert data_reader in flow.tasks
    assert flow.root_tasks() == set([data_reader])
    assert flow.terminal_tasks() == set([data_reader])

def test_data_reader_data_frame_type_failure():
    with pytest.raises(ValueError):
        data_reader = DataReader()
        data_reader.run(
            data_frame_type='fail',
            data_type='csv',
            ticker='one')

def test_data_reader_success_dask_IWM_csv_file():
    data_reader = DataReader()
    data_reader.run(
        data_frame_type='dask',
        data_type='csv',
        ticker='IWM')

def test_data_reader_success_pandas_IWM_csv_file():
    data_reader = DataReader()
    data_reader.run(
        data_frame_type='pandas',
        data_type='csv',
        ticker='IWM')
