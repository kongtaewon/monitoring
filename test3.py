# -*- coding: utf-8 -*-
"""test3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kRaaWevjUj8l-Jsfh8wOHjA0yii2t07j
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
0
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("Dataset.csv", encoding='utf-8')

data.head()

data.dtypes

data.columns.values

data.shape

data.info()

data.describe()

data.isna().sum()

data_sample = data.loc[:, ['Categoria 3',
       'Ziua saptamanii', 'Ziua lunii', 'Luna',
       'Rata inflatiei BNR pe trimestru', 'Rata somaj BIM lunara',
       'Vacanta/zi libera/weekend/ Black Friday',
       'Abnormal situations (alerta, urgenta, razboi, pandemie)']]

data_sample.hist(bins=10, color = '#00517C', figsize=(15, 10))

data_sample.corr().stack()[data_sample.corr().stack()<1].drop_duplicates().abs().sort_values(ascending=False).reset_index()

X = data_sample.drop(columns=['Categoria 3'])

y = data_sample['Categoria 3']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=0)

#pipeline = Pipeline([('imputer', SimpleImputer(strategy="median")), ('std_scaler', StandardScaler()) ])
pipeline = Pipeline([('imputer', SimpleImputer(strategy="median")), ('std_scaler', MinMaxScaler()) ])
X_train = pipeline.fit_transform(X_train)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

X_test = pipeline.transform(X_test)
y_pred = lin_reg.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("mse : " + str(mse))

rmse = np.sqrt(mse)
print("rmse : " + str(rmse))

test_value = [[7,1,1,2.4,9.1,1,0]]   # 336.04
test_predict = lin_reg.predict(test_value)
test_predict

plt.scatter(y_test, y_pred, c='r', alpha=0.4)
plt.xlabel("Actual Categoria 3")
plt.ylabel("Predicted Categoria 3")
plt.title('MULTIPLE LINEAR REGRESSION')
plt.show()

print(lin_reg.coef_)

lin_reg.score(X_test, y_test)

# 요일과 수요 관계
plt.scatter(data_sample[['Ziua saptamanii']], data_sample[['Categoria 3']], c='r', alpha=0.4)
plt.show()

# 분기당 BNR 인플레이션율 과 수요 관계
plt.scatter(data_sample[['Rata inflatiei BNR pe trimestru']], data_sample[['Categoria 3']], c='r', alpha=0.4)
plt.show()

# BIM 월별 실업률 과 수요 관계
plt.scatter(data_sample[['Rata somaj BIM lunara']], data_sample[['Categoria 3']], c='r', alpha=0.4)
plt.show()

knn_reg = KNeighborsRegressor(n_neighbors = 3)

X1 = data_sample.drop(columns=['Categoria 3'])

y1 = data_sample['Categoria 3']

X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, shuffle=True, random_state=1234)

#pipeline = Pipeline([('imputer', SimpleImputer(strategy="median")), ('std_scaler', StandardScaler()) ])
pipeline = Pipeline([('imputer', SimpleImputer(strategy="median")), ('std_scaler', MinMaxScaler()) ])
X1_train = pipeline.fit_transform(X1_train)

knn_reg.fit(X1_train, y1_train)
X1_test = pipeline.transform(X1_test)
y1_pred = knn_reg.predict(X1_test)

mse1 = mean_squared_error(y1_test, y1_pred)
print("mse : " + str(mse1))

rmse1 = np.sqrt(mse1)
print("rmse : " + str(rmse1))

test_value1 = [[7,1,1,2.4,9.1,1,0]]   # 336.04
test_predict1 = knn_reg.predict(test_value1)
test_predict1

plt.scatter(y1_test, y1_pred, c='r', alpha=0.4)
plt.xlabel("Actual Categoria 3")
plt.ylabel("Predicted Categoria 3")
plt.title('KNEIGHBORS REGRESSION')
plt.show()

knn_reg.score(X1_test, y1_test)

data_sample.hist(bins=50, color = '#00517C', figsize=(20,15))

tree_reg = DecisionTreeRegressor()

X2 = data_sample.drop(columns=['Categoria 3'])

y2 = data_sample['Categoria 3']

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, shuffle=True, random_state=42)

#pipeline = Pipeline([('imputer', SimpleImputer(strategy="median")), ('std_scaler', StandardScaler()) ])
pipeline = Pipeline([('imputer', SimpleImputer(strategy="median")), ('std_scaler', MinMaxScaler()) ])
X2_train = pipeline.fit_transform(X2_train)

tree_reg.fit(X2_train, y2_train)
X2_test = pipeline.transform(X2_test)
y2_pred = tree_reg.predict(X2_test)

mse2 = mean_squared_error(y2_test, y2_pred)
print("mse : " + str(mse2))

rmse2 = np.sqrt(mse2)
print("rmse : " + str(rmse2))

test_value2 = [[7,1,1,2.4,9.1,1,0]]   # 336.04
test_predict2 = tree_reg.predict(test_value2)
test_predict2

plt.scatter(y2_test, y2_pred, c='r', alpha=0.4)
plt.xlabel("Actual Categoria 3")
plt.ylabel("Predicted Categoria 3")
plt.title('DECISION TREE REGRESSION')
plt.show()

tree_reg.score(X2_test, y2_test)

forest_reg = RandomForestRegressor()

X3 = data_sample.drop(columns=['Categoria 3'])

y3 = data_sample['Categoria 3']

X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, shuffle=True, random_state=999)

#pipeline = Pipeline([('imputer', SimpleImputer(strategy="median")), ('std_scaler', StandardScaler()) ])
pipeline = Pipeline([('imputer', SimpleImputer(strategy="median")), ('std_scaler', MinMaxScaler()) ])
X3_train = pipeline.fit_transform(X3_train)

forest_reg.fit(X3_train, y3_train)
X3_test = pipeline.transform(X3_test)
y3_pred = tree_reg.predict(X3_test)

mse3 = mean_squared_error(y3_test, y3_pred)
print("mse : " + str(mse3))

rmse3 = np.sqrt(mse3)
print("rmse : " + str(rmse3))

test_value3 = [[7,1,1,2.4,9.1,1,0]]   # 336.04
test_predict3 = forest_reg.predict(test_value3)
test_predict3

plt.scatter(y3_test, y3_pred, c='r', alpha=0.4)
plt.xlabel("Actual Categoria 3")
plt.ylabel("Predicted Categoria 3")
plt.title('RANDOM FOREST REGRESSION')
plt.show()

forest_reg.score(X3_test, y3_test)