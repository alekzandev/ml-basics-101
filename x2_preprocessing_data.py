import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split


class PreprocessingData:
    def __init__(self, path_data: str):
        self.path_data = path_data

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

    def split_data_train_test(self):
        X = self.data.copy().drop(columns=["Rent"])
        y = self.data.copy()["Rent"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=12
        )
        X_train.to_csv("X_train.csv")
        X_test.to_csv("X_test.csv")
        y_train.to_csv("y_train.csv")
        y_test.to_csv("y_test.csv")


if __name__ == "__main__":
    preprocess = PreprocessingData("data.csv")
    preprocess.read_data()
    preprocess.get_nulls()
    preprocess.get_statistics()
    preprocess.get_correlation()
    # preprocess.qqplot()
    preprocess.split_data_train_test()
