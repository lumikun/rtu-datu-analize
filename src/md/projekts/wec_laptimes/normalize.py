import pandas as pd

data = pd.read_csv("raw_data/23_Analysis_Race_Hour 24.CSV", sep=";")
print(data.info())
print(data.shape)
print(data)