import pandas as pd
df = pd.read_csv(
    'https://raw.githubusercontent.com/facebook/prophet/master/examples/example_wp_log_peyton_manning.csv',
    parse_dates=['ds']
)
from dask import dataframe as dd
ddf = dd.from_pandas(df, npartitions=3)
