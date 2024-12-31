# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:11:56 2024

@author: Aayush
"""
"Maximum Number Of Prizes"
"Inout: A positive integer n. Output: The max k such that n cab be represented as a sum a1+ak of k distinct positive integers"

n = int(input())

if n==1:
    print(1)
    print(1)
    quit()
W = n
prizes = []
for i in range (1,n):
    # Check if the remaining value W is greater than twice the current index i
    if W>2*i:
        # If so, append the current index i to the prizes list
        prizes.append(i)
        # Subtract i from W to account for the allocated prize
        W -=i
    else:
        # If W is not greater than twice i, append the remaining value W
        prizes.append(W)
        break
print(len(prizes))
print(" ".join ([str(i) for i in prizes]))