from prefect import Flow, Parameter, unmapped
from prefect.engine.state import State
from prefect.engine.executors import LocalDaskExecutor

from tasks.rescaled_range_tasks import RescaledRange
from tasks.read_data_tasks import DataReader


class ImperativeFlow(Flow):
    def __init__(self, name):
        super().__init__(name)

    def get_flow(self, data_list=['data_one', 'data_two', 'data_three']):

        reader = DataReader()
        rr = RescaledRange()

        data_type = Parameter('data_type', default='pandas')
        self.add_task(data_type)
        self.set_dependencies(
            task=rr(
                mapped=True,
                task_args={'data': reader}
                ),
            upstream_tasks=reader(
                mapped=True,
                task_args={'data_type': unmapped(data_type), 'ticker': data_list})
        )
        return self

    def run(self):
        self.run()
