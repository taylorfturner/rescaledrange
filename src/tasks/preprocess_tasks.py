from prefect import Task 


class PreProcess(Task): 

    def __init__(self): 
        super().__init__()

    def first_diff(self): 
        pass

    def calc_percentage(self): 
        pass
