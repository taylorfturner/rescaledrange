from prefect import Flow, Parameter
from tasks.rescaled_range_tasks import RescaledRange
# from tasks.preprocess_tasks import Preprocess
# from tasks.visualize_tasks import Visualize
# from tasks.metrics_tasks import Metrics


from dask import dataframe as dd
import pandas as pd
df = pd.read_csv('../data/spy.csv')
ddf = dd.from_pandas(df, npartitions=3)

#define the flow
with Flow('rescaled_range') as flow:
    data = RescaledRange(ddf, window=6).run()

# run the flow
flow.run()
