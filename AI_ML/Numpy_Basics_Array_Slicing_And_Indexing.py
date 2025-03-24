# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 22:18:03 2025

@author: Aayush
"""
"Numpy Basics, Array Slicing and Indexing"

import numpy as np 

arr = np.array ([1,2,3,4,5])
print("Array:", arr)

print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Max", np.max(arr))


three_matrix = np.array ([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])

print("3x3 Matrix: \n", three_matrix)

print("Mean of Matrix: ", np.mean(three_matrix))
print("Sum", np.sum(three_matrix))

arr_indexing = np.array([1,2,3,4,5])
print("First element: ", arr_indexing[0])
print("last element: ", arr_indexing[4])

arr_slicing = np.array([10,20,30,40,50,60])
print("First 3 elements: ", arr_slicing[:3])
print("last 3 elements", arr_slicing[:-3])
print("Every second element in the array: ", arr_slicing[::2])

arr_2d_slicing = np.array([[1,2,3,4,5],
                           [6,7,8,9,10],
                           [11,12,13,14,15]])

print("first two rows: ", arr_2d_slicing[:2])
print("last two columns: ", arr_2d_slicing[:, -2:])
print("middle row", arr_2d_slicing[1])