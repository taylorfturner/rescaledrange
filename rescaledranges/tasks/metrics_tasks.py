from prefect import Task 


class Metrics(Task):
    def __init__(self):
        """
        Metrics Subclass of Prefect Task class.

        :Example:
        >>> metrics = Metrics()
        >>> Metrics.run()
        """
        super().__init__()

    def count_sell_signals(self):
        raise NotImplementedError

    def count_buy_signals(self):
        raise NotImplementedError

    def confusion_matrix(self):
        raise NotImplementedError

    def run(self):
        pass
