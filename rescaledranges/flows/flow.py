from prefect import Flow, Parameter, unmapped
from prefect.engine.state import State
from prefect.engine.executors import LocalDaskExecutor

from tasks.rescaled_range_tasks import RescaledRange
from tasks.read_data_tasks import DataReader


class FlowBuilder(Flow):
    def __init__(self):
        pass

    def get_flow(self, flow_name='rescaled_range', data_list=['data_one', 'data_two', 'data_three']):

        flow = Flow(flow_name)
        reader = DataReader()
        rr = RescaledRange()

        data_type = Parameter('data_type', default='pandas')
        data_list = Parameter('data_list', default=['data_one', 'data_two', 'data_three'])
        
        flow.add_task(data_type)
        flow.add_task(reader)
        flow.add_edge(data_type, reader)
        flow.add_edge(data_list, reader)

        flow.set_dependencies(
            task=rr,
            upstream_tasks=[reader],
            mapped=True)

        return flow

    def run(self, flow):
        flow.run()
