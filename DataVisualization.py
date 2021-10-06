import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from scipy import stats

#This dataset is the covid19 affected people's data of 2021 in Bangladesh.
#Our job is to predict death by building multiple Linear regression model
#Here is the data visualization of the new cases vs new deaths and new tests vs new deaths separtely

#Reading dataset from csv file
df = pd.read_csv("Covid19dataBD2021.csv")
#display 10 sample data of the csv file
print (df.head())

x = df['new_cases']   #Taking input column
y = df['new_deaths']  # target Column

slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept

line1 = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, line1)
plt.title("new_cases vs new_deaths")
plt.xlabel("new_cases") #Taking input column
plt.ylabel("new_deaths")
plt.show()

x2 = df['new_tests']   #Taking input column
y = df['new_deaths']  # target Column

slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept

line2 = list(map(myfunc, x))

plt.scatter(x, y, color="red")
plt.plot(x, line2)
plt.title("new_tests vs new_deathsl")
plt.xlabel("new_tests")
plt.ylabel("new_deaths")
plt.show()


