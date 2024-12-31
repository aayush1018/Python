# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:32:45 2024

@author: Aayush
"""

"Binary Search With Duplicates"

def find_first_occurrence(arr, key):
    left, right = 0, len(arr)-1
    result=-1
    
    while left<=right:
        mid = (left+right) // 2
        if arr [mid]== key:
            result = mid
            right = mid -1
        elif arr[mid] < key:
            left = mid+1
        else:
            right = mid - 1
            
    return result

if __name__ == "__main__":
    n = int(input())
    arr = list(map (int, input().split()))
    m = int(input())
    queries = list(map(int, input().split()))
    
    results=[]
    for q in queries:
        index = find_first_occurrence(arr, q)
        results.append(str(index))
    print(" ".join(results))
                