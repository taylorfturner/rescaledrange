import pytest
from .fixtures import fixture_flow
from ...rescaledranges.tasks.read_data_tasks import DataReader


class TestReadData:
    def test_data_reader_no_params(self, fixture_flow):
        data_reader = DataReader()
        fixture_flow.add_task(data_reader)

        assert data_reader in fixture_flow.tasks
        assert len(fixture_flow.tasks) == 1
        assert data_reader in fixture_flow.tasks
        assert fixture_flow.root_tasks() == set([data_reader])
        assert fixture_flow.terminal_tasks() == set([data_reader])

    def test_data_reader_data_frame_type_failure(self):
        with pytest.raises(ValueError):
            data_reader = DataReader(
                data_frame_type='fail',
                data_type='csv',
            )
            data_reader.run(
                ticker='one',
            )

    def test_data_reader_success_dask_IWM_csv_file(self):
        data_reader = DataReader(
            data_frame_type='dask',
            data_type='csv',
        )
        data_reader.run(
            ticker='IWM',
        )

    def test_data_reader_success_pandas_IWM_csv_file(self):
        data_reader = DataReader(
            data_frame_type='pandas',
            data_type='csv',
        )
        data_reader.run(
            ticker='IWM',
        )
