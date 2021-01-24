from prefect import Task

class RescaledRange(Task): 

    def __init__(self, data_frame, **kwargs): 
        self.ddf = data_frame

        self.window = kwargs.get('window')
        self.min_periods = kwargs.get('min_periods', None)
        self.center = kwargs.get('center', False)
        self.win_type = kwargs.get('win_type', None)
        self.axis = kwargs.get('axis', 0)

    def _roll_mean(self):
        return self.ddf.rolling().mean()

    def run(self):

        self.ddf['mean'] = self.ddf['y'].rolling(
            window=self.window,
            min_periods=self.min_periods,
            center=self.center,
            win_type=self.win_type,
            axis=self.axis,
        ).mean()

        self.ddf['mean_adj'] = self.ddf['y'] - self.ddf['mean']

        self.ddf['sum_deviate'] = self.ddf['mean_adj'].rolling(
            window=self.window,
            min_periods=self.min_periods,
            center=self.center,
            win_type=self.win_type,
            axis=self.axis,
        ).mean()

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

        self.ddf['std'] = self.ddf['mean_adj'].rolling(
            window=self.window,
            min_periods=self.min_periods,
            center=self.center,
            win_type=self.win_type,
            axis=self.axis,
        ).std()

        self.ddf['r_s'] = (self.ddf['R'] / self.ddf['std'])

        return {
            'ds': self.ddf['ds'].values,
            'y': self.ddf['y'].values,
            'r_s': self.ddf['r_s'].values
        }
