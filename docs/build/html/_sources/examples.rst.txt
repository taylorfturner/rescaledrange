Example
=======

This is an example Prefect Flow querying data the Yahoo API.

.. code-block:: python

    from prefect import Flow, Parameter, unmapped, task
    from tasks.preprocess_tasks import PreProcess
    from tasks.read_data_tasks import DataReader
    from tasks.rescaled_range_tasks import RescaledRange
    from tasks.visual_tasks import Visualize

    import pandas as pd


    reader = DataReader(data_location="yahoo", data_type="csv", data_frame_type="pandas")
    pre_process = PreProcess()
    rr = RescaledRange()
    visualize = Visualize()


    @task
    def concat_dataframes(data_frames):
        return pd.concat(data_frames)

    with Flow("rescaled_range") as flow:
        ticker_list = Parameter(
            name="ticker_list",
            default=["IWM", "GLD", "TLT", "DBA"]
        )
        data = reader(
            ticker=ticker_list,
            mapped=True
        )
        pre_processed_data = pre_process(data=data, mapped=True)
        rs_data = rr(
            data=pre_processed_data,
            ticker=ticker_list,
            mapped=True,
        )
        reduced_rs_data = concat_dataframes(rs_data)
        visualize(
            ticker_data=reduced_rs_data,
        )


Now let's run our flow composed of prefect tasks. This will not only set variables in our terminal
but it will also produce plotly visuals in our browser.

.. code-block:: python

    state = flow.run()

Now that we have a `state` object initialized in our environment, we can access tasks return values and analyze the
queried data, how it was processed, and the final output. 

.. code-block:: python

    state.result[<task_variable_object>].result

And that's it!
