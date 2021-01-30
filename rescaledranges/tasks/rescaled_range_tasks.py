from prefect.core import Task


class RescaledRange(Task):
    def __init__(self):
        """
        RescaledRange Subclass of Prefect Task class.

        :Example:
        >>> rescaled_ranges = RescaledRange()
        >>> rescaled_ranges.run(data)
        """
        super().__init__()

    def run(self, data):
        """[summary]

        :param data: [description]
        :type data: [type]
        :return: [description]
        :rtype: [type]
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
