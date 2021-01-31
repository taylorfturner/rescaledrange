from prefect import Task

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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

    def signal_summary(self):
        raise NotImplementedError

    def visualize_graph(self, flow):
        return flow.visualize()

    def plot(self, ticker_data):
        #TODO: move this to Dash
        # https://dash.plotly.com/
        plot_data_df = pd.DataFrame(ticker_data)
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(
            go.Scatter(x=plot_data_df['ds'], y=plot_data_df['ts'], name="ts data"),
            secondary_y=False,
        )
        fig.add_trace(
            go.Scatter(x=plot_data_df['ds'], y=plot_data_df['r_s'], name="r_s data"),
            secondary_y=True,
        )
        fig.show()

    def run(self, ticker_data):
        self.plot(ticker_data)
