# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 21:59:46 2025

@author: Aayush
"""

"Merging and Joining DataFrames in Pandas"

#ex1 - merge()
import pandas as pd

employees = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Dept': ['HR', 'IT', 'IT', 'Finance']
})

salaries = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Salary': [50000, 70000, 65000, 60000]
})

merged_df = pd.merge(employees, salaries, on ="ID")
print(merged_df)
print("----------------------")

#ex2 Different types of join
#inner join
salaries_1 = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Salary': [50000, 70000, 65000, 80000]
})

inner_join = pd.merge(employees, salaries_1, on = "ID", how = "inner")
print(inner_join)
print("----------------------")

#left join

left_join = pd.merge(employees, salaries_1, on ="ID", how = "left")
print(left_join)
print("----------------------")

#right join

right_join = pd.merge(employees, salaries_1, on ="ID", how = "right")
print(right_join)
print("----------------------")

#outer join

outer_join = pd.merge(employees, salaries_1, on = 'ID', how = "outer")
print(outer_join)
print("----------------------")

#ex3 - join() - joining on index

employees.set_index("ID", inplace = True)
salaries_1.set_index("ID", inplace = True)

joined_df = employees.join(salaries_1, how = "inner")
print(joined_df)
