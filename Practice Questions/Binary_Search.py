# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:57:42 2024

@author: Aayush
"""
"Binary Search. Search a key in a sorted array of keys"

def binary_serach (arr, key):
    #initializing the left and right pointers for binary search
    left, right, = 0, len(arr)-1
    
    while left<= right:
        #calculate the middle index
        mid = (left+right) // 2
        #check if the middle element is the key that we are looking for
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1  #searching in the right half
        else:
            right = mid -1 #searching in the left half
    return -1 # if the key is not found

if __name__ == "__main__":
    n = int(input())
    #read the sorted distinct integers as a list
    seq = list(map(int, input().split()))
    # read the no of queries
    m = int(input())
    # read the queries as a list of integers
    queries = list (map(int, input().split()))
    results = []
    for q in queries:
        # perform binary search for each query in the sorted array
        index = binary_serach(seq, q)
        #append the result (index or -1) to the results list
        results.append(str(index))
    print(" ".join(results))