from prefect import Flow, Parameter, unmapped, task
from tasks.preprocess_tasks import PreProcess
from tasks.read_data_tasks import DataReader
from tasks.rescaled_range_tasks import RescaledRange
from tasks.visual_tasks import Visualize

import pandas as pd


reader = DataReader()
pre_process = PreProcess()
rr = RescaledRange()
visualize = Visualize()


@task
def concat_dataframes(data_frames):
    return pd.concat(data_frames)

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
        default=['SPY', 'TLT', 'IWM', 'DBA', 'SHY', 'USO']
    )
    flow.add_task(data_type)
    data = reader(
        ticker=ticker_list,
        mapped=True
    )
    pre_processed_data = pre_process(
        data=data,
        mapped=True
    )
    rs_data = rr(
        data=pre_processed_data,
        ticker=ticker_list,
        mapped=True,
    )
    reduced_rs_data = concat_dataframes(rs_data)
    visualize(
    	ticker_data=reduced_rs_data,
    )

state = flow.run()
state.visualize()

# To see data output from tasks
# access through `state.result[task_name]`
state.result[rs_data]
