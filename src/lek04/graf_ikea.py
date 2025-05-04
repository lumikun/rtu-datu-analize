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
print(selection)
sns.scatterplot(data=selection, x="laiks", y="skaits")
plt.show()