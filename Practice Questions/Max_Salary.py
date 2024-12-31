# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:18:23 2024

@author: Aayush
"""
"Maximum Salary. Compile the largest integer by concatenating the given integers"
"Input: A sequence of positive integers. Output: The largest integer that can be obtained by concatenating the given integers in some order"

n = int(input())
lst= [int (i) for i in input().split()]

def isGreaterOrEqual (digit, max_digit):
    return int(str(digit)+str(max_digit)) >= int(str(max_digit) + str(digit))

def largest_number(lst):
    ans = []
    while lst !=[]:
        max_digit = 0
        for digit in lst:
            if isGreaterOrEqual(digit, max_digit):
                max_digit = digit
                
        ans.append(max_digit)
        lst.remove(max_digit)
        
    return ans
print (''.join ([str (i) for i in largest_number(lst)]))
        
