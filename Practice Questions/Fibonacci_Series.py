# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:14:50 2024

@author: Aayush
"""

"Fibonacci Series"
" compute the nth fibonnaci number"
"Input- An integer n. Output - nth Fibonacci Number"


    
def fibonacci_Series (number):
    a , b = 0 , 1
    for i in range (number-1):
        c = a+b
        b,a=c,b  #example of tuple unpacking in python.
    print(c)
        
number= int (input())
if number <= 1:
    print(number)
        
fibonacci_Series(number)
