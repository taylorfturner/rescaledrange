from prefect import Flow, Parameter
from tasks.preprocess_tasks import Preprocess
from tasks.rescaled_range_tasks import RescaledRange
from tasks.visualize_tasks import Visualize
from tasks.metrics_tasks import Metrics


#define the flow
with Flow('rescaled_range') as flow: 
    data = RescaledRange(ddf, window=3).run()
