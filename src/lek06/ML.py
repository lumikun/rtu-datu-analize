from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

# demo data about flower petals, lengths and petal species
iris = load_iris()
print(type(iris))
print("Keys: ", iris.keys())
# Data(data), target(species_numerical), target_names(species_name)


print("data size in 'data': ", iris.data.shape)
print("data size in 'target': ", iris.target.shape)
# svarigi apmacibas un testejot, lai sakrit izmeri - ja nav vienads rindu skaits = problemas
print(iris.data[0])
print("Col names (features): ", iris.feature_names)
print("Clasificators (target): ", iris.target_names)

data = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(data)

data["target"] = iris.target
print(data)
# as dots / scatterplot
plt.scatter(data['sepal length (cm)'], data['sepal width (cm)'], c=data['target'], cmap='viridis')
# cmap = color_map, c = categorization
plt.scatter(data['petal length (cm)'], data['petal width (cm)'], c=data['target'], cmap='magma')
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.title("Iris dataset")
plt.colorbar(label="Class")
plt.show()

data["s"] = data["sepal length (cm)"] / data["sepal width (cm)"]
data["p"] = data["petal length (cm)"] / data["petal width (cm)"]

