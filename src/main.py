from prefect import Flow, Parameter, unmapped
from tasks.rescaled_range_tasks import RescaledRange
from tasks.read_data_tasks import DataReader


ticker_list = ['SPY', 'TLT']
reader = DataReader()
rr = RescaledRange()

with Flow('rescaled_range') as flow:

    data_type = Parameter('data_type', default='pandas')
    flow.add_task(data_type)

    data = reader.map(
        data_type=unmapped(data_type), 
        ticker=ticker_list
    )
    rr_data = rr.map(data=data)

flow.visualize()
flow.run()
