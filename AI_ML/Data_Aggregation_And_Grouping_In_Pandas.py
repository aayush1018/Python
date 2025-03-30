# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:17:41 2025

@author: Aayush
"""

"Data Agrregration and Grouping In Pandas"

#ex1 - Grouping Data
import pandas as pd

data = {
    'Category': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home'],
    'Product': ['Laptop', 'Phone', 'Shirt', 'Jeans', 'Table'],
    'Price': [1000, 500, 50, 40, 200]
}

df = pd.DataFrame(data)

grouped_df = df.groupby("Category")["Price"].mean()
print("Grouped DF: \n", grouped_df)
print("-------------------")

#ex2 Aggregation functions

grouped_df_1 = df.groupby("Category")["Price"].agg(['mean', 'sum', 'count'])
print(grouped_df_1)
print("-------------------")

#ex3 Pivot Tables and Cross Tabulation

pivot = df.pivot_table(values = "Price", index ="Category", aggfunc ="sum")
print(pivot)

