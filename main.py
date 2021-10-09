#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

#Problem: Predict death no. using the sample data of the excel file which is the 
#covid 19 affected people's data in Bangladesh of 2021
#see the sampledatapdf file to get idea about sample data

#ignore .idea and venv folders which are the required files to run the project in the python IDE.

# Covid19deathPrediction2021UsingMultipleLinearRegression
# This Project's  dataset is the covid19 affected people's data of 2021 in Bangladesh.
# Our job is to predict death by building multivariable/multiple Linear regression model

# Value assigning
prev_new_cases = 0
prev_new_tests = 0
prev_new_casesCoEff = 0.0
prev_new_testsCoEff = 0.0
Prev_Death = 0
Counter= 0
decision=0

# model building
# set your input values

def setupInputValues():
    print("Covid19 Death Prediction in Bangladesh using  Multiple Linear Regression Machine Learning model\n")
    # Taking input from the user as integer
    print("For validating the model set different new input:\n")
    new_cases = int(input("Enter new_cases no. on a specific date:\n"))
    new_tests=  int(input("Enter new_tests no. on that date:\n"))
    modelBuild(new_cases, new_tests)

def modelBuild(new_cases, new_tests):
    # Reading dataset from csv file
    df = pd.read_csv("Covid19dataBD2021.csv")
    X = df.iloc[:,1:3]  #Getting all rows of 2nd,3rd column
    y = df['new_deaths'] #target Column

    regrModel = linear_model.LinearRegression() #regression model
    regrModel.fit(X, y)
    predictedNewDeath = int(regrModel.predict([[int(new_cases), int(new_tests)]]))
    print("Predicted Death no:")
    print(predictedNewDeath)
    CoefficientsList = regrModel.coef_  # Taking Coeeficient value
    if Counter==0:
        print("\n Do You want to check Coefficients(Verify the model) of input variables? ")
        print("\n Write 1 to check otherwise write 0: ")
        decision = int(input(""))
        if decision==1:
            modelCoefficientChecking(decision, CoefficientsList, predictedNewDeath, new_cases, new_tests)
        else: # for decision 0
            return

    else: # means counter=1
        decision=2
        modelCoefficientChecking(decision, CoefficientsList, predictedNewDeath, new_cases, new_tests)


#Coeeficient Checking
def modelCoefficientChecking(decision, CoeefficientsList, predictedNewDeath, new_cases, new_tests):
    global Counter, Prev_Death
    global prev_new_cases, prev_new_tests, prev_new_casesCoEff, prev_new_testsCoEff
    if decision == 1:

        if  Counter == 0:
            prev_new_cases = new_cases
            prev_new_tests = new_tests
            prev_new_casesCoEff = CoeefficientsList[0]
            prev_new_testsCoEff = CoeefficientsList[1]
            Prev_Death = predictedNewDeath
            Counter = Counter + 1

        setupInputValues()
    elif decision== 2:
        print("Previous Death:")
        print(Prev_Death)
        print("\nCoeff. of Previous new_cases:")
        print(prev_new_casesCoEff)
        print("\nCoeff. of Previous new_tests:")
        print(prev_new_testsCoEff)
        CalculatedDeath=Prev_Death + abs(prev_new_cases-new_cases)*prev_new_casesCoEff + abs(prev_new_tests-new_tests)*prev_new_testsCoEff
        print("Prev_Death + (prev_new_cases-new_cases)*prev_new_casesCoEff + (prev_new_tests-new_tests)*prev_new_testsCoEff=")
        print(CalculatedDeath)
        print("=predictedNewDeath(approx.) ")
        print(int(predictedNewDeath))
    else:

        print("\n")

#Program starting
print("Covid19 Death Prediction in Bangladesh using  Multiple Linear Regression Machine Learning model\n")
# Taking input from the user as integer
new_cases = int(input("Enter new_cases no. on a specific date:\n"))
new_tests = int(input("Enter new_tests no. on that date:\n"))

modelBuild(new_cases, new_tests) # output checking:(6566, 41014) # 7248, 39278

