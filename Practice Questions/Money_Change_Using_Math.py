# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:19:54 2024

@author: Aayush
"""

''' Compute the min no of coins neededd to change the given value into coins with denominations 1,3 and 4
Input: An integer money
Output: The min no of coins with denominations 1,3,4 that changes the money'''

import math

money = int(input())
denominations = [1,3,4]
minCoins = [0] + [math.inf]*money

for i in range (1, money+1):
    for j in denominations:
        if i>=j:
            coins=minCoins[i-j]+1
            if coins<minCoins[i]:
                minCoins[i] = coins
                
print(minCoins[money])
            