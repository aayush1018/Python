# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 14:30:21 2025

@author: Aayush
"""

"Data Visualization in Pandas"

#ex1 Basic Line Plot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {"Year": [2018,2019,2020,2021,2022],
        "Sales":[200,250,300,400,500]}

df = pd.DataFrame(data)

df.plot(x ="Year", y = "Sales", kind ="line", marker = "o", figsize = (8,5))
plt.title("Sales over time")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid()
plt.show()

#ex2 Bar Plot (Comparison of Categories)

df.plot(x = "Year", y ="Sales", kind ="bar", color ="skyblue", figsize = (8,5))
plt.title("Annual Sales")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()

#ex3 Scatter Plot (For Relationships between two variables)

df["Profit"] = [50,70,90,130,180]
df.plot(x="Sales", y = "Profit", kind = "scatter", color= "red", figsize=(8,5))
plt.title("Sales vs profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

#ex4 Pie chart(Proportions)

df.set_index("Year")["Sales"].plot(kind = "pie", autopct = "%1.1f%%", colormap ="viridis")
plt.ylabel("")
plt.title("Sales Distribution")
plt.show()

#ex5 histogram
np.random.seed(42)
sales_data = np.random.normal(loc = 250, scale=50, size =100)
df_hist = pd.DataFrame({"Sales": sales_data})
df_hist["Sales"].plot(kind="hist", bins=10, color="purple", edgecolor="black")
plt.title("Sales Distribution")
plt.xlabel("Sales Value")
plt.xlabel("Frequency")
plt.show()