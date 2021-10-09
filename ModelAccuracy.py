import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Reading dataset from csv file
# This dataset is the covid19 affected people's data of 2021 in Bangladesh.
# Our job is to predict death by building multivariable Linear regression model
#ACCURACY CHECKING for the model

df = pd.read_csv("Covid19dataBD2021.csv")
X = df.iloc[:, 1:3]  # Getting all rows of 2nd,3rd column
y = df['new_deaths']  # target Column

# Splitting the dataset into training and test set.
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2)
regrModel = linear_model.LinearRegression()  # regression model
#training data fitting to the model
regrModel.fit(x_train, y_train)
# Predicting the Test set result
y_pred = regrModel.predict(x_test)
#ACCURACY Checking
print('Train Score: ', regrModel.score(x_train, y_train))
print('Test Score: ', regrModel.score(x_test, y_test))





