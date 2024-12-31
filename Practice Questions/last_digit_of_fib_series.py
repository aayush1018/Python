# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:33:37 2024

@author: Aayush
"""

"Last digit of a large fibonacci number"
''' Given an integer n, find the last digit of a large fibonacci number F(n). The Fibonnaci sequence is defined as follow 
F(0)=1
f(1)= 1
Input
A single integer n where 0<n<10^8
Output
Output a singal integer, the last digit of F(n)
'''

number1 = int (input())
if number1<=1:
    print(number1)
    
def last_digit_of_fib_series(number1):
    a,b=0,1
    for i in range (number1-1):
        c= a+b
        c = c % 10  #use to obtain the last digit. The modulus operator returns the remainder
        b , a =c , b
    print (c)
    
last_digit_of_fib_series(number1)
    