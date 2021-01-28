from prefect import Task


class Visualize(Task): 
    def __init__(self):
        """
        Visualize Subclass of Prefect Task class.

        :Example:
        >>> viz = Visualize()
        >>> viz.run()
        """
        super().__init__()
    
    def equity_curve(self): 
        raise NotImplementedError