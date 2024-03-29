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
        """[summary]

        :param column_name: [description]
        :type column_name: [type]
        :return: [description]
        :rtype: [type]
        """
        return self.data[column_name].shift(1).cumsum() / \
            (self.data["counter"].cumsum()-1)

    def mean_adjust(self, column_name):
        """[summary]

        :param column_name: [description]
        :type column_name: [type]
        :return: [description]
        :rtype: [type]
        """
        return self.data[column_name] - self.data["mean"]

    def calc_r(self, column_name):
        """[summary]

        :param column_name: [description]
        :type column_name: [type]
        :return: [description]
        :rtype: [type]
        """
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
        """[summary]
        """
        def _cum_std(row): 
            return (row["cum_sum_mean_adj_sqr"] / row["cum_sum_counter"]) ** .5
        return self.data.apply(_cum_std, axis=1)        

    def run(self, data, ticker):
        """[summary]

        :param data: [description]
        :type data: [type]
        :return: [description]
        :rtype: [type]
        """

        def counter_column(row):
            row["counter"] = int(1)
            return row

        self.data = data

        self.data = self.data.apply(counter_column, axis=1)
        self.data["ts_pcnt"] = self.data["Close"].pct_change()

        self.data["mean"] = self.cummean("ts_pcnt")
        self.data["mean_adj"] = self.mean_adjust("ts_pcnt")
        self.data["sum_deviate"] = self.data["mean_adj"].cumsum()
        self.data["R"] = self.calc_r("mean_adj")
        self.data["mean_adj_sqr"] = self.data["mean_adj"] ** 2
        self.data["cum_sum_mean_adj_sqr"] = self.data["mean_adj_sqr"].cumsum()
        self.data["cum_sum_counter"] = self.data["counter"].cumsum()
        self.data["std"] = self.cumstd()
        self.data["H"] = (self.data["R"] / self.data["std"])
        self.data["ticker"] = ticker

        self.data = self.data[["Date", "counter", "H", "ticker", "Close"]]
        self.data = self.data.dropna(subset=["H"])
        
        return self.data
