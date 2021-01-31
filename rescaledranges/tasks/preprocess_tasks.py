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

    def first_diff(self):
        raise NotImplementedError

    def calc_percentage(self):
        raise NotImplementedError
