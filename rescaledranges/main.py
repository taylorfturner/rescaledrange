from prefect import Flow, Parameter, unmapped
from tasks.rescaled_range_tasks import RescaledRange
from tasks.read_data_tasks import DataReader
from tasks.visual_tasks import Visualize


reader = DataReader()
rr = RescaledRange()
visualize = Visualize()

with Flow('rescaled_range') as flow:
    data_frame_type = Parameter(
        name='data_frame_type',
        default='pandas'
    )
    data_type = Parameter(
        name='data_type',
        default='csv'
    )
    ticker_list = Parameter(
        name='ticker_list',
        default=['SPY', 'TLT', 'IWM']
    )
    flow.add_task(data_type)
    data = reader(
        data_frame_type=unmapped(data_frame_type),
        data_type=unmapped(data_type),
        ticker=ticker_list,
        mapped=True
    )
    rs_data = rr(
        data=data,
        mapped=True
    )
    visualize(
    	ticker_data=rs_data,
    	mapped=True
    )

flow.run()
