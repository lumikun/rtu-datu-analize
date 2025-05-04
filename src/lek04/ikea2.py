import pandas as pd
import re

f = "ikea_preces_2.xlsx"
data = pd.read_excel(f)

# principā varētu izfiltrēt ar regx, Reali stulbs veids ka filtret????
filtrs = data["apraksts"].str.contains("3,5 vietu")
print(list(data[filtrs].index))

data["apr.sad."] = data["apraksts"].str.split(",")

data["merv"] = pd.Series(dtype="object")
data["krasas"] = pd.Series(dtype="object")
data["kat"] = pd.Series(dtype="object")
print(data.dtypes)