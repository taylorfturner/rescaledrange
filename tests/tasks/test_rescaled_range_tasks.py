import pytest
from prefect import Flow, Parameter
from .fixtures import fixture_flow, iwm_test_data
from ...rescaledranges.tasks.rescaled_range_tasks import RescaledRange

class TestRescaledRanges:
    def test_rescaled_range_data_processing_instantiation(self, fixture_flow):
        rr = RescaledRange()
        fixture_flow.add_task(rr)

        assert rr in fixture_flow.tasks
        assert len(fixture_flow.tasks) == 1
        assert rr in fixture_flow.tasks
        assert fixture_flow.root_tasks() == set([rr])
        assert fixture_flow.terminal_tasks() == set([rr])

    def test_rescaled_range_data_processing(self, iwm_test_data):
        rr = RescaledRange()
        rs_data = rr.run(
            data=iwm_test_data,
            ticker="IWM",
        )
