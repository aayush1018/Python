# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 18:06:00 2025

@author: Aayush
"""

"Time Series Data in Pandas"

#ex2 - Creating DateTime Index
#converting a column to DateTime

import pandas as pd
data = {"Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "Sales": [200,250,300]}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

df.set_index("Date", inplace = True)

print(df)
print("----------------------")

#ex2 Date based indexing and slicing
#selecting data for a specific date
print(df.loc["2023-01-02"])
print("----------------------")
#slicing data by date range
print(df.loc["2023-01-01":"2023-01-03"])
print("----------------------")

#ex3 Creating a Date Range

date_range = pd.date_range(start="2023-01-01", periods = 5 , freq = "D") # D means daily intervals. We can use H - hourly, W - weekly, M - Monthly and Y - Yearly

print(date_range)
print("----------------------")

#ex4 Resampling (Agrregating Data)

resampled_data = df.resample("ME").sum()
print("Resampled Data:\n", resampled_data)
print("----------------------")

#Ex5 extracting date components

df["Year"] = df.index.year
df["Month"] = df.index.month
df["Day"] = df.index.day
print(df)