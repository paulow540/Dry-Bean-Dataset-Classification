import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import pickle 

import seaborn as sns

# def beans_prediction(beans):
beansdata = pd.read_excel("Dry_Bean_Dataset.xlsx")

X_iris = beansdata.drop('Class', axis=1)
y_iris = beansdata["Class"]

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state=1)

print(Xtrain.shape, "sdfghjfghjhj")
from sklearn.naive_bayes import GaussianNB # 1. choose model class
modelGau = GaussianNB() # 2. instantiate model
modelGau.fit(Xtrain, ytrain) # 3. fit model to data
pickle.dump(modelGau, open("model.pkl","wb"))
model = pickle.load(open("model.pkl", "rb"))

# y_model = model.predict(Xtest)
# print(y_model,"okkkkkkkkkkkkkkkkkkkk")

# from sklearn.metrics import accuracy_score
# accuracy_score(ytest, y_model)
# print(accuracy_score(ytest, y_model), "accuracy_score#####")
# new_sample = Xtest.copy() 
# new_sample['species'] = ytest
# new_sample.iloc[16]
# y_model = model.predict(Xtest.iloc[16].values.reshape(1,16))
# print("Your new specie is ",y_model[0], " flower.")

# return model.predict(y_model)
