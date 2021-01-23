from prefect import Flow, Parameter
from tasks.rescaled_range_tasks import RescaledRange
from tasks.visualize_tasks import Visualize


with Flow('rescaled_range') as flow: 
    
    ticker = Parameter('ticker')

    
    data = RescaledRange.run()


flow.run(parameters=dict())
