# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:12:40 2024

@author: Aayush
"""
"Find the maximum dot product of two sequences of numbers"
"Input: Two sequences of n positive integers: price1.. princen and clicks1,... clicksn"
"Output: The maximum value of price1.c1+pricen.cn where c1, cn is a permutations of clicks c1, cn"

n = int(input())
a = [int(i) for i in input().split()]
b= [int (i) for i in input().split()]
a.sort()
b.sort()
ans= sum([a[i]*b[i] for i in range (n)])
print(ans)