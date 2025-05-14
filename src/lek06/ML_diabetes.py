from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt

diabetes = load_diabetes()

print(diabetes.data.shape)

data = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print(data)
data["target"] = diabetes.target

plt.scatter(data["bmi"], data["bp"], c=data["target"], cmap="viridis")
plt.xlabel("BMI")
plt.ylabel("BP")
plt.title("Diabetes dataset")
plt.colorbar(label="Class")
plt.show()