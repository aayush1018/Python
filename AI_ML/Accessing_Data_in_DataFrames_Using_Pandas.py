# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 17:04:15 2025

@author: Aayush
"""

"Accessing Data in DataFrames"


import pandas as pd

data = {
        "Product": ['Laptop', 'Phone', 'Tablet'],
        "Price": [100, 500, 400],
        "Stock": [50,200,150]
        }

df= pd.DataFrame(data)
print(df["Price"]) # using brackets

print(df.Price) # using Dot notation

print(df[["Price","Stock"]]) #selecting multiple columns
print("----------------------")
#LOC - labed based indexing
print(df.loc[0]) # select first row
print(df.loc[1:2]) # selecting multiple rows

#iLOC - integer based indexing
print("---------------------")
print(df.iloc[0]) # first row
print(df.iloc[1:3]) # rows from index 1 to 2


#Selecting Specific Values
print("-------------------")
print(df.at[1, "Price"]) # label based selection
print(df.iat[1,1]) # Position based selection