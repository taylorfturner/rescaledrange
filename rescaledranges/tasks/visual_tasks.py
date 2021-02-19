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
        raise NotImplementedError

    def line_plot(self, ticker_data):
        plot_data_df = pd.DataFrame(ticker_data)
        for ticker in plot_data_df["ticker"]:
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(
                go.Scatter(x=ticker["Date"], y=ticker["Close"], name="ts data"),
                secondary_y=False,  
            )
            fig.add_trace(
                go.Scatter(x=ticker["Date"], y=ticker["H"], name="H data"),
                secondary_y=True,
            )
            fig.show()

    def heatmap_plot(self, ticker_data):
        df = pd.DataFrame(ticker_data)
        print (df.head())
        fig = go.Figure(data=go.Heatmap(
            z=df["H"],
            x=df["Date"],
            y=df["ticker"],
            colorscale="RdBu"))
        fig.show()

    def run(self, ticker_data):
        # self.line_plot(ticker_data)
        self.heatmap_plot(ticker_data)
