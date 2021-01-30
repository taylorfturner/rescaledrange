from prefect import Flow, Parameter, unmapped
from tasks.rescaled_range_tasks import RescaledRange
from tasks.read_data_tasks import DataReader


reader = DataReader()
rr = RescaledRange()

with Flow('rescaled_range') as flow:

    data_type = Parameter(
        name='data_type',
        default='pandas'
    )
    ticker_list = Parameter(
        name='ticker_list',
        default=['SPY', 'TLT', 'IWM']
    )
    
    flow.add_task(data_type)

    data = reader(
        data_type=unmapped(data_type),
        ticker=ticker_list,
        mapped=True
    )

    rs_data = rr(
        data=data,
        mapped=True
    )

flow.visualize()
state = flow.run()
