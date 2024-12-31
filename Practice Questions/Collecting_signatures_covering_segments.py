# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:31:12 2024

@author: Aayush
"""
"Find the minimum number of points needed to cover all given segments on a line"
"Input: A sequence of n segments on a line. Output: A set of minimum size such that each segment contains a point"

n = int (input())
lst = []

for i in range (n):
    a,b = [ int (i) for i in input().split()]
    lst.append((a,b))

# Sort the list of coordinate pairs by the second element (b) of each tuple    
lst.sort (key = lambda x:x[1])

index =0
coordinates = []

while index < n:
    curr = lst [index]
    # Continue to check for overlapping intervals
    while index <n-1 and curr[1]>=lst[index+1][0]:
        index+=1
    coordinates.append(curr[1])
    index+=1
print(len(coordinates))
print(" ".join([str(i) for i in coordinates]))