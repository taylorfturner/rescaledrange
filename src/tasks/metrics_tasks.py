from prefect import Task 


class Metrics(Task): 

    def __init__(self): 
        super().__init__()

    def count_sell_signals(self): 
        pass

    def count_buy_signals(self): 
        pass
