from prefect import Flow, Parameter
from tasks.rescaled_range_tasks import RescaledRange
from tasks.read_data_tasks import DataReader
from dask import dataframe as dd
import pandas as pd

reader = DataReader()
rr = RescaledRange()

#define the flow
with Flow('rescaled_range') as flow:

    data_type = Parameter('data_type', default='dask')
    flow.add_task(data_type)

    data = reader(data_type)
    rr_data = rr(data)

flow.visualize()
flow.run()
