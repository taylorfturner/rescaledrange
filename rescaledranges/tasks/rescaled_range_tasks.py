from prefect.core import Task


class RescaledRange(Task):
    def __init__(self):
        """
        RescaledRange Subclass of Prefect Task Class.

        :Example:
        >>> rescaled_ranges = RescaledRange()
        >>> rescaled_ranges.run(data)
        """
        super().__init__()
        self.data = None

    def cummean(self, column_name):
        return self.data[column_name].shift(1).cumsum() / \
            (self.data['counter'].cumsum()-1)

    def mean_adjust(self, column_name):
        return self.data[column_name] - self.data['mean']

    def calc_r(self, column_name):
        return self.data[column_name].rolling(
                window=6,
                min_periods=6,
                center=False,
                win_type=None,
                axis=0,
            ).max() - self.data[column_name].rolling(
                window=6,
                min_periods=6,
                center=False,
                win_type=None,
                axis=0,
            ).min()

    def cumstd(self):
        def _cum_std(row): 
            return (row['cum_sum_mean_adj_sqr'] / row['cum_sum_counter']) ** .5
        return self.data.apply(_cum_std, axis=1)

    def run(self, data):
        """[summary]

        :param data: [description]
        :type data: [type]
        :return: [description]
        :rtype: [type]
        """
        self.data = data

        self.data['mean'] = self.cummean('ts_pcnt')
        self.data['mean_adj'] = self.mean_adjust('ts_pcnt')
        self.data['sum_deviate'] = self.data['mean_adj'].cumsum()
        self.data['R'] = self.calc_r('mean_adj')
        self.data['mean_adj_sqr'] = self.data['mean_adj'] ** 2
        self.data['cum_sum_mean_adj_sqr'] = self.data['mean_adj_sqr'].cumsum()
        self.data['cum_sum_counter'] = self.data['counter'].cumsum()
        self.data['std'] = self.cumstd()
        data['r_s'] = (data['R'] / data['std'])

        return {
            'ds': self.data['ds'].values,
            'ts': self.data['ts'].values,
            'ts_pcnt': self.data['ts_pcnt'].values,
            'r_s': self.data['r_s'].values
        }
