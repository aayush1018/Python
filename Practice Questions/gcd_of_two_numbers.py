# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:56:50 2024

@author: Aayush
"""

"Greatest Common Divisor"
" Input: Two positive integers a and b. Output: The greatest common divisor a and b"

"Using Euclidean algorithm"

a,b = [int (i) for i in input().split()]

def gcd_of_two_numbers (a,b) :
    while (b):
        a,b=b, a % b
    return a
    
print(gcd_of_two_numbers(a, b))