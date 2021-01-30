from prefect import Flow, Parameter, unmapped
from prefect.engine.state import State
from prefect.engine.executors import LocalDaskExecutor

from tasks.rescaled_range_tasks import RescaledRange
from tasks.read_data_tasks import DataReader


class FlowBuilder(Flow):
    def __init__(self, flow_name='rescaled_range'):
        super().__init__(flow_name)

    @classmethod
    def get_flow(cls, data_list=['data_one', 'data_two', 'data_three']):

        reader = DataReader()
        rr = RescaledRange()

        data_type = Parameter('data_type', default='pandas')
        data_list = Parameter('data_list', default=['data_one', 'data_two', 'data_three'])

        cls.add_edge(upstream_task=data_type, downstream_task=reader)
        cls.add_edge(upstream_task=data_list, downstream_task=reader)

        cls.set_dependencies(
            task=rr,
            upstream_tasks=[reader],
            mapped=True)

        return True

    @classmethod
    def run(cls):
        cls.run()
