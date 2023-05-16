#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:46:42 2023

@author: mdridwanrahman
"""

import numpy as np
import pandas as pd
import mlxtend
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score as acc
from mlxtend.feature_selection import SequentialFeatureSelector as sfs

# Read data
df = pd.read_csv('/Users/mdridwanrahman/Desktop/Research/congestion_data_4_19_2.csv')
df1 = df.drop(['Scenario', 'SwitchNum', 'cost'], axis = 1) 

X = df1.loc[:,['LMP82', 'LMP96', 'Dg12', 'Bc15', 'Bc16', 'Bc36', 'Bc39', 'Bc58', 'Bc81', 'Bc116', 'Bc119', 'Bc132', 'Bc133', 'Bc152', 'Bc153', 'Bc165', 'Bc184']]

y = df1[['SwitchId']]

# split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# create a Random Forest Classifier model with default parameters
rfc = RandomForestClassifier()

# fit the model to the training data
rfc.fit(X_train, y_train)

# make predictions on the testing data
y_pred = rfc.predict(X_test)

# evaluate the accuracy of the model
accuracy = acc(y_test, y_pred)
print('Accuracy:', accuracy)
