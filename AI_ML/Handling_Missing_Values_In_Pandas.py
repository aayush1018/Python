# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:09:25 2025

@author: Aayush
"""

"Handling Missing Values in Pandas"

#ex1 detecting missing values
import pandas as pd
import numpy as np

data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Price': [1000, 500, np.nan, 700],  # Missing Price for Tablet
    'Stock': [50, 200, 150, np.nan]  # Missing Stock for Monitor
}

df = pd.DataFrame(data)

print(df.isna()) #check where the values are NAN
print("------------------------------")
print(df.isna().sum()) # count missing values in each column
print("------------------------------")
#ex2 - remove missing values
df_cleaned = df.dropna()
print("Clean dataset:\n" , df_cleaned)
print("------------------------------")
df.dropna(axis=1, inplace = True) #axis = 1 means columns

#ex3 filling missing values
df1 = pd.DataFrame(data)
df_filled = df1.fillna({"Price": df1["Price"].mean(), "Stock": 0})
print("Filled Dataset:\n", df_filled)
