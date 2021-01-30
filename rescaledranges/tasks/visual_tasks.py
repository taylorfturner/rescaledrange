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

    def plot(self, state):
        plot_data = state.result[rs_data].result[0]
        plot_data_df = pd.DataFrame(plot_data)
        fig = px.line(plot_data_df, x="ds", y="r_s")
        fig.show()
