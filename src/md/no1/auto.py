import pandas as pd 

auto_data = pd.read_csv("auto.csv", index_col="_id")
df = auto_data.query("GAZ == 'BMW'")
val = 2000.0
df = df.query("'1961' <= @val")

print(len(df.index))
