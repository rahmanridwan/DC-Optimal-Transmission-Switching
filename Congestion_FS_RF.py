#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:35:27 2023

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
data = pd.read_csv("/Users/mdridwanrahman/Desktop/Research/congestion_data_4_19_2.csv")
df1 = data.loc[data['SwitchNum'] == 0]
#df2 = df1.drop(['Scenario', 'SwitchNum', 'cost', 'SwitchId'], axis = 1) 

X = df1.loc[:,'LMP1':'Bc186']

y = df1[['SwitchId']]

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    

y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

print('Training dataset shape:', X_train.shape, y_train.shape)
print('Testing dataset shape:', X_test.shape, y_test.shape)

# Build RF classifier to use in feature selection
clf = RandomForestClassifier(n_estimators=100, n_jobs=-1)

# Build step forward feature selection
sfs1 = sfs(clf, k_features=25,forward=True,floating=False,verbose=2,scoring='accuracy',cv=5)

# Perform SFFS
sfs1 = sfs1.fit(X_train, y_train)

# Print accuracies for each feature subset
print("\nAccuracy scores for each feature subset:\n")
for i in range(1, len(sfs1.subsets_)):
    print(f"Subset {i}: {sfs1.subsets_[i]['avg_score']:.4f}")
    
# Find and print the maximum accuracy and the corresponding subset
max_accuracy_subset = list(sfs1.subsets_.values())[np.argmax([s['avg_score'] for s in sfs1.subsets_.values()])]
print(f"\nMaximum accuracy of {max_accuracy_subset['avg_score']:.4f} is achieved with subset: {max_accuracy_subset['feature_names']}")

# Save results to excel file
results_df = pd.DataFrame.from_dict(sfs1.subsets_).T
results_df.index.name = 'subset'
results_df.to_excel('/Users/mdridwanrahman/Desktop/Research/Feature_Selection.xlsx')

# Save the maximum accuracy and its feature subset to the Excel file
max_accuracy_subset_df = pd.DataFrame({'Maximum Accuracy': max_accuracy_subset['avg_score'], 'Feature Subset': [max_accuracy_subset['feature_names']]})
max_accuracy_subset_df.index.name = 'subset'
max_accuracy_subset_df.to_excel('/Users/mdridwanrahman/Desktop/Research/Feature_Selection_Maximum_Accuracy.xlsx')
