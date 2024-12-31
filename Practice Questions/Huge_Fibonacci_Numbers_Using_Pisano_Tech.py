# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:30:19 2024

@author: Aayush
"""

"Compute the n-th Fibonacci number modulo m"
"Input: integers n and m. Output - m-th Fibonacci number modulo m"

def pisano_period (a):
    # returns the length of the pisano period for modulo m
    previous, current = 0,1
    for i in range (0, a*a):
        previous, current = current, (previous + current) % a
        # the period always starts with 0,1
        if (previous == 0 and current == 1):
            return i+1

def fibonnacci_series(b,a):
    # finding the pisano period
    period= pisano_period(a)
    #reducing the pisano period
    b = b % period
    # computing the fibonacci number for the reduced n
    previous, current = 0,1
    
    for i in range (b):
        previous, current = current, (previous + current) % a
        
    return previous

b,a= [int (i) for i in input().split()]

result = fibonnacci_series(b, a)
print (result)