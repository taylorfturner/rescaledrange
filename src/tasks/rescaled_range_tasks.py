from prefect import Task

class RescaledRange(Task): 

    def _rolling_average(self): 
        pass

    def _mean_adjust_series(self):
        pass

    def _calc_range_series(self):
        pass

    def _calc_stdev(self):
        pass

    def _calc_rescaled_range(self):
        pass

    def run(self, min_max_window, sigma_window, average_window):
        """[summary]

        :param min_max_window: [description]
        :type min_max_window: [type]
        :param sigma_window: [description]
        :type sigma_window: [type]
        :param average_window: [description]
        :type average_window: [type]
        """

        return 'data'
