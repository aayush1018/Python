# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:00:12 2024

@author: Aayush
"""

"Majority Element Problem"
"Input: A sequence of n integers. Output: 1, if there is an element that is repeated more than n/2 times, and 0 otherwise"

def majority_element(sequence):
    #initialize the candidate for majority element and count
    candidate = None
    count = 0
    #find a candidate for the majority element
    for num in sequence:
        # if count is zero we set the current number as the candidate
        if count == 0:
            candidate = num
            # increment count if the current no is the candidate or decrement it
        count+= (1 if num == candidate else -1)
        # verify if the candidate is indeed the majority element
    if sequence.count (candidate) > len(sequence) //2:
        return 1
    else:
        return 0
n = int(input())
input_sequence = list(map(int,input().split()))
result = majority_element(input_sequence)
print(result)