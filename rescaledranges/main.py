from prefect import Flow, Parameter, unmapped, task
from tasks.read_data_tasks import DataReader
from tasks.rescaled_range_tasks import RescaledRange
from tasks.visual_tasks import Visualize

import pandas as pd


reader = DataReader(data_location="yahoo", data_type="csv", data_frame_type="pandas")
rr = RescaledRange()
visualize = Visualize()


@task
def concat_dataframes(data_frames):
    return pd.concat(data_frames)

with Flow("rescaled_range") as flow:
    ticker_list = Parameter(
        name="ticker_list",
        default=["IWM", "GLD", "TLT", "DBA"]
    )
    data = reader(
        ticker=ticker_list,
        mapped=True
    )
    rs_data = rr(
        data=data,
        ticker=ticker_list,
        mapped=True,
    )
    reduced_rs_data = concat_dataframes(rs_data)
    visualize(
        ticker_data=reduced_rs_data,
    )

state = flow.run()
