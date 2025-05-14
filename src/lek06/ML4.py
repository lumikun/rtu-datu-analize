import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

data = load_diabetes()
x = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
# -------------------
print("Base prediction")
capture = model.intercept_
koef = pd.Series(model.coef_, index=x.columns)
print(capture)
print("Coeficient")
print(koef.sort_values(ascending=False))
# Graphics
sns.barplot(x=koef.values, y=koef.index)
plt.xlabel("Koeficienti")
plt.ylabel("Parametri")
plt.show()
y_predict = model.predict(x_test)
# -------------------
mse = mean_squared_error(y_test, y_predict)
mae = mean_absolute_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)
# factual vs predicted
sns.scatterplot(x=y_test, y=y_predict)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
plt.xlabel("Factual Value")
plt.ylabel("Predicted value")
plt.show()
# error distribution
error = y_test - y_predict
sns.histplot(error, kde=True, bins=20)
plt.xlabel("Error")
plt.ylabel("rate")
plt.show()