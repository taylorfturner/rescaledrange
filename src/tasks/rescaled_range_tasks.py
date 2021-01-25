from prefect import Task

import random
random.seed(30)

class RescaledRange(Task): 

    def __init__(self, data_frame, **kwargs):
        """
        Instantiation of class for calculating rescaled range 
            on provided time series.

        :Example:
        >>> rr = RescaledRange(dask_dataframe, window=6)
        >>> rr.run()
        """
        self.ddf = data_frame

        self.window = kwargs.get('window')
        self.min_periods = kwargs.get('min_periods', 6)
        self.center = kwargs.get('center', False)
        self.win_type = kwargs.get('win_type', None)
        self.axis = kwargs.get('axis', 0)
    
    def _mean_adjust(self, time_series, mean_series):
        """
        A private method take the difference between two
        series.

        :param time_series: the data series to be processed
        :type code_list: Dask.Series, required
        :return: single series that is the difference between two 
        series.
        :rtype: Dask.Series
        """
        return self.ddf[time_series] - self.ddf[mean_series]

    def run(self):
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
        self.ddf['counter'] = 1

        self.ddf['ts'] = ((self.ddf['ts'] / self.ddf['ts'].shift(1)) - 1)
        self.ddf = self.ddf[self.ddf['ds'] != '2020-01-21']
        self.ddf['mean'] = (self.ddf['ts'].shift(1).cumsum() / (self.ddf['counter'].cumsum()-1))
        self.ddf['mean_adj'] = self._mean_adjust('ts', 'mean')
        self.ddf['sum_deviate'] = self.ddf['mean_adj'].cumsum()
        self.ddf['R'] = self.ddf['mean_adj'].rolling(
                window=self.window,
                min_periods=self.min_periods,
                center=self.center,
                win_type=self.win_type,
                axis=self.axis,
            ).max() - self.ddf['mean_adj'].rolling(
                window=self.window,
                min_periods=self.min_periods,
                center=self.center,
                win_type=self.win_type,
                axis=self.axis,
            ).min()
        self.ddf = self.ddf[self.ddf['ds'] >= '2020-01-23']
        self.ddf['mean_adj_sqr'] = self.ddf['mean_adj'] ** 2
        self.ddf['cum_sum_mean_adj_sqr'] = self.ddf['mean_adj_sqr'].cumsum()
        self.ddf['cum_sum_counter'] = self.ddf['counter'].cumsum()
        
        def _cum_std(row): 
            return (row['cum_sum_mean_adj_sqr'] / row['cum_sum_counter']) ** (1/2)

        self.ddf['std'] = self.ddf.apply(_cum_std, axis=1)
        self.ddf['r_s'] = (self.ddf['R'] / self.ddf['std'])

        return {
            'ds': self.ddf['ds'].values,
            'ts': self.ddf['ts'].values,
            'r_s': self.ddf['r_s'].values
        }
