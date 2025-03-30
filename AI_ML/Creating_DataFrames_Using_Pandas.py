# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 16:45:49 2025

@author: Aayush
"""

"Creating A DataFrame using Pandas"

#ex1 
#useful when working with structured data like excel
import pandas as pd
import numpy as np

data = {
        "Product": ['Laptop', 'Phone', 'Tablet'],
        "Price": [100, 500, 400],
        "Stock": [50,200,150]
        }

df= pd.DataFrame(data)
print(df) 

#ex2
# useful when data is already in form of list
data2 = [["Laptop",1000, 50],
         ["Phone", 500, 200],
         ["Tablet", 400, 150]]

df1 = pd.DataFrame(data2, columns = ["Product", "Price", "Stock"])

print(df1)

#ex3
#From a numpy array 

data3= np.array([[1000,50], [500,200], [300,150]])

df2 = pd.DataFrame(data3, columns = ["Products", "Stock"])
print(df2)

# the following commands can be used to inspect a dataframe

print(df.head())
print("--------------------------------")
print(df.tail(2))
print("--------------------------------")
print(df.info())
print("--------------------------------")
print(df.describe())
print("--------------------------------")
print(df.shape)
print("--------------------------------")
print(df.columns)
