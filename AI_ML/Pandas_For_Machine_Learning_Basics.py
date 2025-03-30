# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 14:52:41 2025

@author: Aayush
"""

"Pandas for Machine Learning Basics"

#ex1 Feature Engineering
#Handling Categorical Data
import pandas as pd

df = pd.DataFrame({"Category": ["A", "B", "A", "C", "B"]})

df_encoded = pd.get_dummies(df,columns = ["Category"])
print(df_encoded)
print("----------------------")
#Feature Scaling (Standardization and Normalization)

from sklearn.preprocessing import StandardScaler, MinMaxScaler

df= pd.DataFrame({"Sales":[100,200,300,400,500]})

scaler = StandardScaler()
df["Sales_Standardized"] = scaler.fit_transform(df[["Sales"]])

min_max_scaler=MinMaxScaler()
df["Sales_Normalized"] = min_max_scaler.fit_transform(df[["Sales"]])

print(df)

#ex2 exporting data in Pandas

df.to_csv("cleaned_data.csv", index= False)

#exporting to excel
df.to_excel("cleaned_data.xlsx", index = False)

#exporting to Json
df.to_json("cleaned_data.json", orient = "records")