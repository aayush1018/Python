# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 16:23:46 2025

@author: Aayush
"""

"Basics Of Pandas"
#ex1
import pandas as pd

data = [10,20,30,40,50]

series = pd.Series(data)

print(series)

#ex2 
data_frame ={
    "Name": ['Alice', 'BOB', 'Charlie'],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000 ]}

df = pd.DataFrame(data_frame)

print(df)

#ex3 - checking data in data_frame
print("--------------------------------")
print("\n Dataframe head: ",df.head())
print("--------------------------------")
print("\n Dataframe info: ",df.info())
print("--------------------------------")
print("\n Datafram Describe: \n", df.describe())
print("--------------------------------")
print("\n Dataframe Shape: ", df.shape)