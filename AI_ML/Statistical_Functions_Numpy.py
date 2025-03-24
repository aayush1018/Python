# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 14:38:24 2025

@author: Aayush
"""

"Numpy statistical functions"

import numpy as np

data = np.array([10,20,30,40,50])

mean_value = np.mean(data)
print("Mean Value: ", mean_value)

median_value = np.median(data)
print("Meadian_Value: ", median_value)

std_dev = np.std(data)
variance = np.var(data)

print("Standard Deviation: ", std_dev)
print("Variance: ", variance)

#min, max and percentiles

min_value = np.min(data)
max_value = np.max(data)
percentile_25 = np.percentile(data,25)
percentile_75 = np.percentile(data, 75)

print("Min Value: ", mean_value)
print("Max_Value: ", max_value)
print("Percentile 25: ", percentile_25)
print("Percentile 75: ", percentile_75)

# correlations and covariance 

dataset = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
correlation = np.corrcoef(dataset)
covariance = np.cov(dataset)

print("Correlation Matrix: ", correlation)
print("Covariance Matrix: ", covariance)