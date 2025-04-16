import pandas as pd
from termcolor import colored as c

# print(c(f"kaut, kāds teksts", "green"))

data = pd.read_csv("auto_imports_mainits.csv", header=0)
print(data)
# print(data.info()) # varbut noderīgi

# print(c("\n\tTykšumi", "blue"))
# print(c("T/F table", "blue"))
# print(data.isnull())
# print(c("T/F table kur ir tukšumi", "blue"))
# print(data.isnull().any())
# print(c("Cik kolonās ir tuksumi", "blue"))
# print(data.isnull().any().sum())
# print(data.isnull().sum())
#print(data.isnull().sum().sum())
# min rindām, kas var traucēt strādāt ir lielākais tukšumu skaits kolonā
# Max ir kopejais tukšumu skaits.

#apkopojums = data["normalized-losses"].notnull()
#print(apkopojums)
#print(data[~apkopojums])

# NEAT
print(c("\n\tSarežģīts kopsavilk.", "green"))
apkopojums = pd.DataFrame(data.isnull().sum(), data.columns[data.isnull().any()], columns=["skaits"])
print(apkopojums)
# 37 iztrukst
print(data.describe())
# count - skaits cik vērtības
# mean ir vidējais
# std -deviācīja
# min, max - self explanatory
# 50% medians
# 25% un 75% lower and upper median
#data["normalized-losses"].dropna(inplace=True) # Dzēš tukšos.
data = data.drop("normalized-losses", axis=1)
apkopojums = pd.DataFrame(data.isnull().sum(), data.columns[data.isnull().any()], columns=["skaits"])
print(data.shape)
data2 = data.copy()
#del data2["stroke"]
# data2 = data2.dropna() # Dzēš visas rindas kur tukšums.
#print(data2.shape) # 3.9% tukšums
uzksaitjumi = list(data2.columns[data2.isnull().any()])
for col_name in uzksaitjumi:
     del data2[col_name]
print(data2.shape)
print(uzksaitjumi)

# TODO: Check this.
# data2 = data.copy()
# data2 - data2.drop(columns=uzksaitjumi)
# print(data2.shape)

# data2 = data2.drop([0,1])
# print(data2.head)
# print(data2.shape)
data2 = data.copy()
print(c("Rindiņa", "red"))
print(c("loc", "green"))
print(data2.loc[0]) # var izmantot nosauk bāzētas info atrašanai
print(c("iloc", "green"))
print(data2.iloc[0]["make"]) # obligāti jābūt ciparam []
print(c("at", "green"))
print(data2.at[0, "make"]) # 0. rinda, make kolonna
print(c("Nejauši izvēlēta rinda", "green"))
print(data2.sample(3)) # 3 rando, rindas.

print(c("Iloc", "red"))
for i in range(52, 54):
     print(data2.iloc[i])


print("\n\n\n")
bad = ["N/A", "NA", "--"]
data2 = pd.read_csv("auto_imports_mainits.csv", na_values=bad)
print(data2.iloc[52])

# Vidējais aritmētiskais
# bore
insert_val = round(data2["bore"].mean(), 2)
data2["bore"].fillna(insert_val, inplace=True) 
print("\n\n")
print(data2.iloc[52])
print("\n\n")
# mediana
# stroke
insert_val = round(data2["stroke"].median())
data2["stroke"].fillna(insert_val, inplace=True)
print(data2.iloc[52])
print("\n\n")
# visbiežāk lietotā vērtība
# num-of-doors - stringi
insert_val = data2["num-of-doors"].mode()[0]
data2["num-of-doors"].fillna(insert_val, inplace=True)
print(data2.iloc[60])

# viss sarežģīts
