import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("ikea_preces_3.xlsx")
print(data.dtypes)
print(data.describe())
count_data = data.select_dtypes(include=["float64", "int64"])
print(count_data.corr())

#sns.set_style("darkgrid")
#plt.rcParams["figure.figsize"] = (10, 8)
#sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm")
#plt.show()
#sns.scatterplot(data=data)
#plt.show()
# Neder scatterplot, neatlasot/neierobežojot info, jo ir daudz datu, kas parklājas. (turklāt x asī iet indeksa nr.)

selection = data[["cena", "laiks"]].groupby("laiks").count()
selection = selection.reset_index()
selection = selection.rename(columns={"cena": "skaits"})
#print(selection)
#sns.scatterplot(data=selection, x="laiks", y="skaits")
#plt.show()

mers_1 = (data["izm1"].notna() & data["izm2"].isna() & data["izm3"].isna()).sum()
mers_2 = (data["izm2"].notna() & data["izm2"].notna() & data["izm3"].isna()).sum()
mers_3 = (data["izm3"].notna() & data["izm2"].notna() & data["izm3"].notna()).sum()

laiks = (data["laiks"].notna()).sum()
tilpums = (data["tilpums"].notna()).sum()
print(mers_1, mers_2, mers_3, laiks, tilpums)

data_gfx = pd.DataFrame({\
    "kategorija":["1 izm", "2 izm", "3 izm", "st.", "l"],\
    "skaits":[mers_1, mers_2, mers_3, laiks, tilpums],\
        })
#sns.set_palette("Set3")
#plt.pie(data_gfx["skaits"], labels=data_gfx["kategorija"], autopct="%.1f%%")
#plt.title("Precu skaits")
#plt.show()

#sns.histplot(data["cena"], bins=10)
#plt.show()

#robezas = [0, 5, 10, 20, 30, 50, 75, 100, 700]
#data["sadalijums"] = pd.cut(data["cena"], bins=robezas, include_lowest=True)
#print(data["sadalijums"].value_counts())
#sns.histplot(data["cena"], bins=robezas)
#plt.show()

# izmantojam tikai prieks sevis, bet prieks prezentacijas vajag but vienadam robezam
# robezas = [0, 2.5, 5, 7.5, 10, 15, 20, 30, 50, 75, 100]
# data["sadalijums"] = pd.cut(data["cena"], bins=robezas, include_lowest=True)
# print(data["sadalijums"].value_counts())
# sns.histplot(data["cena"], bins=robezas)
# plt.show()

robezas = [0, 2.5, 5, 7.5, 10]
nosaukumi = ["<2.5", "2.5-5.0", "5.0-7.5", "7,5-10.0"]
data["sadalijums"] = pd.cut(data["cena"], bins=robezas, include_lowest=True)
skaiti = data["sadalijums"].value_counts()
print(data["sadalijums"].value_counts())

# plt.pie(skaiti, labels=nosaukumi, autopct="%.1f%%")
# plt.show()

sns.boxplot(data=data, x="sadalijums", y="cena")
plt.show()