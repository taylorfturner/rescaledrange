from prefect import Task 


class Metrics(Task):
    def __init__(self):
        """
        Metrics Subclass of Prefect Task class. This should include 
        everything from count of buy / sell signals, confusion matrix, 
        and any other metric related to the success of failure of
        the system on the particular ticker.

        :Example:
        >>> metrics = Metrics()
        >>> Metrics.run()
        """
        super().__init__()

    def run(self):
        raise NotImplementedError
