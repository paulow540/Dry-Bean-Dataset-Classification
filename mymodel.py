import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

import seaborn as sns

def beans_prediction(beans):
    beansdata = pd.read_excel("Dry_Bean_Dataset.xlsx")

    X_iris = beansdata.drop('Class', axis=1)
    y_iris = beansdata["Class"]

    from sklearn.model_selection import train_test_split
    Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state=1)

    from sklearn.naive_bayes import GaussianNB # 1. choose model class
    model = GaussianNB() # 2. instantiate model
    model.fit(Xtrain, ytrain) # 3. fit model to data
    y_model = model.predict(Xtest)
    print(Xtest)

    from sklearn.metrics import accuracy_score
    accuracy_score(ytest, y_model)
    print(accuracy_score(ytest, y_model), "accuracy_score#####")

    return model.predict(Xtest)
