from prefect import Task


class Visualize(Task): 
    def __init__(self):
        """
        Visualize Subclass of Prefect Task class.

        :Example:
        >>> viz = Visualize()
        >>> viz
        >>> <Task: Visualize>
        """
        super().__init__()
    
    def equity_curve(self): 
        raise NotImplementedError

    def flow_visualize(self, flow):
        return flow.visualize()

    def signal_summary(self):
        raise NotImplementedError
