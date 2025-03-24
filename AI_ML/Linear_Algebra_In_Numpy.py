# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 14:24:25 2025

@author: Aayush
"""

"Numpy Linear Algebra"

#ex1 - Matrix Multiplication

import numpy as np

A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
              [7,8]])

result = np.dot(A, B)

print("result: ", result)

#ex2 - finding the determinant

det_A = np.linalg.det(A)

print("Determinant of A: ", det_A)

#ex3 - inversion of a matrix

inv_A = np.linalg.inv(A)

print("Inversion Matrix: ", inv_A)

#ex4 - Eigenvalues and EigenVectors
#used in principal component analysis to find important features in ML

eigenvalues, eigenvectors = np.linalg.eig(A)

print("EigenValues: ", eigenvalues)
print("EigenVectors: ", eigenvectors)