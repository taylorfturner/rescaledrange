from prefect import Task


class PreProcess(Task):
    def __init__(self):
        """
        PreProcess Subclass of Prefect Task class.

        :Example:
        >>> prep = PreProcess()
        >>> prep.run()
        """
        super().__init__()

    def run(self, data):
        """Primary run method required due
        to prefect task class inheritance.

        :param data: Time series data
        :type data: pd.DataFrame, required
        """
        def counter_column(row):
            row["counter"] = int(1)
            return row

        data = data.apply(counter_column, axis=1)
        data["ts_pcnt"] = data["Close"].pct_change()

        return data
