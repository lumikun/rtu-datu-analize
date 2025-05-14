from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
# nodrosinas datu sadalisanu
from sklearn.neighbors import KNeighborsClassifier
# K closest neighbours algo
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()

x = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names
x_use = x[:,:2] # all rows, but 0 - 1 
# print(x_use)
#split data
x_train, x_test, y_train, y_test = train_test_split(x_use, y, test_size=0.3, random_state=42)
# train = for learning
# test = for testing
# test_size = % how much data for testing 0.2 -> 20%
print(iris.data.shape)
print(x_train.shape)

model = KNeighborsClassifier(n_neighbors=3)
# how many neighbors to account for
model.fit(x_train, y_train)
# train model
y_expect = model.predict(x_test)
# learn model, and give test data. Save result
print("Paredzetas vertibas: ", y_expect)

print("Accuracy: ", accuracy_score(y_test, y_expect))
# fro k=3->80%

print("Confusion matrix:")
print(confusion_matrix(y_test, y_expect))
# shows how often it's correct and how often not(and where)
# [[10  0  0] 10 out of 10 correct
#  [ 0  7  2] 2nd param 7 correct, 2 incorrect 7/9 corrrect
#  [ 0  4  7]] 3rd param 4 correct, 7 incorrect 7/11
print("Clasification report: ")
print(classification_report(y_test, y_expect, target_names=target_names))
# precision - how many correct from all guesses
# recall - from category how many were correct
# f1-score - balance between precision un recall
# 2 * (precision * recall) / (precision + recall)
# support - how many examples all together

data = pd.DataFrame(x_test, columns=[feature_names[0], feature_names[1]])
data["actual"] = y_test
data["predicted"] = y_expect
data["correct"] = data["actual"] == data["predicted"]

for i, correct in enumerate([True, False]):
    filtered = data[data["correct"] == correct]
    marker = 'o' if correct else 'x'
    plt.scatter(filtered[feature_names[0]], filtered[feature_names[1]], marker=marker, c=filtered["predicted"], cmap="viridis")

plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.show() 
# k = 1, 5, 7