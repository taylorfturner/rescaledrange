from prefect import Task

import random
random.seed(30)

class RescaledRange(Task): 

    def __init__(self, data_frame, **kwargs): 
        self.ddf = data_frame

        self.window = kwargs.get('window')
        self.min_periods = kwargs.get('min_periods', 6)
        self.center = kwargs.get('center', False)
        self.win_type = kwargs.get('win_type', None)
        self.axis = kwargs.get('axis', 0)
    
    def _mean_adjust(self, time_series, mean_series):
        return self.ddf[time_series] - self.ddf[mean_series]

    def run(self):

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

        self.ddf['mean_adj_sqr'] = self.ddf['mean_adj'] ** 2
        self.ddf['std'] = (self.ddf['mean_adj_sqr'].cumsum() / self.ddf['counter'].sum()) ** (1/2)

        self.ddf['r_s'] = (self.ddf['R'] / self.ddf['std'])

        return {
            'ds': self.ddf['ds'].values,
            'ts': self.ddf['ts'].values,
            'r_s': self.ddf['r_s'].values
        }
