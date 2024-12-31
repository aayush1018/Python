# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:51:17 2024

@author: Aayush
"""

"Speeding up randomized quick sort"
'''Input: An integer array with n elements that may contain duplicates.
Output: Sorted array (generated using a modification of randomizedquicksort) that works in O(nlogn) expected time '''

import random

def randomized_quick_sort(arr):
    if len (arr) <=1:
        return arr
    else:
        pivot = random.choice(arr)
        # three way partiotioning
        less = []
        equal = []
        greater = []
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        #recursively apply the same logic to left and right parts
        return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)
    
if __name__ == "__main__":
    n = int(input())
    user_input = input()
    array = list(map(int, user_input.split()))
    
    sorted_array = randomized_quick_sort(array)
    print(" ".join(map(str, sorted_array)))