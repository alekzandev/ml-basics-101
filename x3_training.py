import pandas as pd
from pycaret.regression import * 

class TrainModel:
    def __init__(self, data_clean: pd.DataFrame):
        self.data_clean = data_clean
        
    
    def setup_train(self):
        self.setup_experiment = setup(self.data_clean, target = 'Rent')
        

if __name__ == "__main__":
    data = pd.read_csv('data_clean.csv')
    trainmodel = TrainModel(data)
    trainmodel.setup_train()
