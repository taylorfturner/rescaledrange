import pytest
from prefect import Task, Flow
from rescaledranges.tasks.rescaled_range_tasks import RescaledRange


@pytest.fixture
def flow():
    return Flow('test_rescaled_range_task')

def test_rescaled_range_no_params(flow):
    rr = RescaledRange()
    flow.add_task(rr)
    assert rr in flow.tasks
    assert len(flow.tasks) == 1
