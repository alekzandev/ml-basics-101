import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split


class PreprocessingData:
    def __init__(self, path_data: str):
        self.path_data = path_data
        self.categories: list  = ['Floor','Area Type','Area Locality','City','Furnishing Status','Tenant Preferred','Point of Contact']
        self.cat_dummies: list = ['Area Type','City','Furnishing Status','Tenant Preferred','Point of Contact']

    def read_data(self):
        self.data = pd.read_csv(self.path_data)
        print(self.data.info())

    def get_nulls(self):
        print(self.data.isnull().sum())

    def get_statistics(self):
        print(f""" Mean: {self.data['Rent'].mean():,.2f} """)
        print(f""" Median: {self.data['Rent'].median():,.2f}""")
        print(f""" Min: {self.data['Rent'].min():,.2f}""")
        print(f"""Max: {self.data['Rent'].max():,.2f}""")

    def get_correlation(self):
        sns.pairplot(self.data, corner=True).savefig("PairPlot.png")
        print(self.data.corr())
        plt.close()

    def qqplot(self):
        # fig, ax = plt.subplots(1,2, sharey=True)
        qq = stats.probplot(self.data["Rent"], plot=plt)
        plt.close()
        qq_log = stats.probplot(np.log(self.data["Rent"]), plot=plt)
        # ax[0] = stats.probplot(self.data['Rent'])
        # ax[1] = stats.probplot(np.log(self.data['Rent']))
        plt.show()
        
        
    def explore_categorical(self):
        for i in self.categories:
            print(f'\t {i}')
            print(self.data[i].value_counts(),'\n\n')
            
    def cleaning_data(self):
        self.data = self.data.loc[self.data['Point of Contact'] != 'Contact Builder'].copy()
        self.data = self.data.loc[self.data['Area Type'] != 'Built Area'].copy()
        self.data = self.data.loc[self.data['Point of Contact'] != 'Contact Builder'].copy()
        self.data = self.data.drop(columns= ['Area Locality'])
        
    def transform_data(self):
        self.data[['floor_placed','floor_number']] = self.data['Floor'].str.split(' out of ', expand = True)
        self.data.loc[self.data['floor_placed'] == 'Ground', 'floor_placed'] = 1 
        self.data.loc[self.data['floor_placed'] == 'Lower Basement', 'floor_placed'] = 0
        self.data.loc[self.data['floor_placed'] == 'Upper Basement', 'floor_placed'] = self.data.loc[self.data['floor_placed'] == 'Upper Basement', 'floor_number']
        self.data['floor_placed'] = self.data['floor_placed'].astype(int)
        self.data = self.data.loc[~self.data['floor_number'].isna()]
        self.data['floor_number'] = self.data['floor_number'].astype(int)
        self.data = self.data.drop(columns = ['Floor','Posted On'])
        #self.data['Posted On'] = pd.to_datetime(self.data['Posted On'])
        print(self.data.info())
        
    #def get_features_from_date(self):
        #print(self.data['Posted On'].min())
        #print(self.data['Posted On'].max())
        
    def create_dummies(self):
        for i in self.cat_dummies:
            self.data = pd.concat([self.data,pd.get_dummies(self.data[i], prefix = f'{i}')],axis = 1)
            self.data = self.data.drop(columns=[i])
        #print(pd.get_dummies(self.data['Area Type']))        
        print(self.data.info())
        
    def split_data_train_test(self):
        X = self.data.copy().drop(columns=["Rent"])
        y = self.data.copy()["Rent"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=12
        )
        X_train.to_csv("X_train.csv",index = False)
        X_test.to_csv("X_test.csv", index = False)
        y_train.to_csv("y_train.csv",index = False)
        y_test.to_csv("y_test.csv", index = False)
        
        
    


if __name__ == "__main__":
    preprocess = PreprocessingData("data.csv")
    preprocess.read_data()
    preprocess.get_nulls()
    preprocess.get_statistics()
    preprocess.get_correlation()
    # preprocess.qqplot()
    #preprocess.split_data_train_test()
    preprocess.explore_categorical()
    preprocess.cleaning_data()
    preprocess.transform_data()
    #preprocess.get_features_from_date()
    preprocess.create_dummies()