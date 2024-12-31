# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:02:59 2024

@author: Aayush
"""

"Least Common Multiple"
"Input: Two positive integers a and b. Output: The least common multiple of a and b"

a,b = [int (i) for i in input().split()]

def least_common_multiple(a,b):
    if b==0:
        return a
    c = a % b
    return least_common_multiple(b, c)

if a>b:
    gcd= least_common_multiple(a, b)
else:
    gcd = least_common_multiple(b, a)
    
print(a*b//gcd)