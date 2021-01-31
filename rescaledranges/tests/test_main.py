import pytest


@pytest.fixture('test_data')
def test_main():




from prefect.core.edge import Edge

assert e in flow.tasks
assert t in flow.tasks
assert l in flow.tasks
assert len(flow.tasks) == 3

assert flow.root_tasks() == set([e])
assert flow.terminal_tasks() == set([l])

assert len(flow.edges) == 2
assert Edge(upstream_task=e, downstream_task=t, key="x") in flow.edges
assert Edge(upstream_task=t, downstream_task=l, key="x") in flow.edges