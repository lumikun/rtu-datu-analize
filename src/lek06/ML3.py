import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = {
    'age': [25, 30, np.nan, 35, 40, 45, 60, 50, 60, 18],
    'income': [5000, 6000, 5200, np.nan,8000, 8200, 8500, 8800, 3300, 1500],
    'sex': ['m', 'f', 'f', 'f', 'm', 'm', 'f', 'm', 'f', 'm'],
    'target': [0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
}
data = pd.DataFrame(data)
print(data)
