# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 13:43:58 2025

@author: Aayush
"""

"Broadcasting"

import numpy as np

#ex1
arr = np.array([1,2,3,4,5])

new_arr = arr +10
print("Original Array: ", arr)
print("New Array: ", new_arr)

#ex2
matrix = np.array ([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

vector = np.array([10,20,30])

result = matrix + vector

print("Original Matrix: ", matrix)
print("Broadcasted Result: ", result)

#ex3 - broadcast across columns

column_vector = np.array ([[10],
                           [20],
                           [30]])

result_col_matrix = matrix + column_vector

print("Original Matrix: ", matrix)
print("Column matrix: ", result_col_matrix)

#ex4
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

result_mul_arr = arr1*arr2

print("Element wise multiplication: ", result_mul_arr)