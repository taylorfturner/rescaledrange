from prefect import Flow, task, Parameter
from dask import dataframe as dd
import pandas as pd

@task
def read_dask():
    df = pd.read_csv('spy.csv')
    return dd.from_pandas(df, npartitions=3)

@task
def rescale_range(data):
    """
    A private method to reorder the fred dataset codes
    so that the left join of all the datasets works
    correctly and we do not drop data from higher-frequence
    datasets.

    :param code_list: list of FRED dataset codes
    :type code_list: list, required
    :return: list of ordered FRED dataset codes, ordered
    by frequency from high-frequency to low-frequency
    :rtype: list
    """
    window=6
    min_periods=6
    center=False
    win_type=None
    axis=0

    data['counter'] = 1

    data['ts'] = ((data['ts'] / data['ts'].shift(1)) - 1)
    data = data[data['ds'] != '2020-01-21']
    data['mean'] = (data['ts'].shift(1).cumsum() / (data['counter'].cumsum()-1))
    data['mean_adj'] = data['ts'] - data['mean']
    data['sum_deviate'] = data['mean_adj'].cumsum()
    data['R'] = data['mean_adj'].rolling(
            window=window,
            min_periods=min_periods,
            center=center,
            win_type=win_type,
            axis=axis,
        ).max() - data['mean_adj'].rolling(
            window=window,
            min_periods=min_periods,
            center=center,
            win_type=win_type,
            axis=axis,
        ).min()
    data = data[data['ds'] >= '2020-01-23']
    data['mean_adj_sqr'] = data['mean_adj'] ** 2
    data['cum_sum_mean_adj_sqr'] = data['mean_adj_sqr'].cumsum()
    data['cum_sum_counter'] = data['counter'].cumsum()
    
    def _cum_std(row): 
        return (row['cum_sum_mean_adj_sqr'] / row['cum_sum_counter']) ** (1/2)

    data['std'] = data.apply(_cum_std, axis=1)
    data['r_s'] = (data['R'] / data['std'])

    return {
        'ds': data['ds'].values,
        'ts': data['ts'].values,
        'r_s': data['r_s'].values
    }


with Flow("My Flow") as flow:
    data = read_dask()
    output = rescale_range(data)
    
    print (output)

flow.visualize()
flow.run()