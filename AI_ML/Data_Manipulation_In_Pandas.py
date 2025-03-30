# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 21:50:34 2025

@author: Aayush
"""

"Data Manipulation In Pandas"

import pandas as pd

#ex1 Filtering and selecting rows
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Price': [1000, 500, 300, 700],
    'Stock': [50, 200, 150, 100]
}

df = pd.DataFrame(data)

filtered_dataset = df[df["Price"]>500]
print(filtered_dataset)
print("--------------------")

#filtering with multiple conditions
filtered_dataset_1 = df[(df["Price"]>500) & (df["Stock"]>50)]
print(filtered_dataset_1)
print("--------------------")
#ex2 Adding and removing columns

df ["Discounted Price"] = df ["Price"] * 0.9
print("Discounted price:\n", df)
print("--------------------")

#removing a column
df.drop(columns=["Discounted Price"], inplace = True)
print(df)
print("--------------------")

#ex3 sorting data

df_sorted = df.sort_values(by = "Price", ascending = False)
print("Descending Order:\n", df_sorted)
print("--------------------")

#Sorting of Multiple Columns
df_sorted_1 = df.sort_values(by = ["Stock", "Price"] , ascending = [False, True])
print("Multiple Columns sorted: \n", df_sorted_1)