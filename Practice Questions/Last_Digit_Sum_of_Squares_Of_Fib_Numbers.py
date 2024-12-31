# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 00:30:47 2024

@author: Aayush
"""

"Sum Of Squares of Fibonacci Numbers"
"Input: An int n. Output: last digit of sum of squares of the fibonacci numbers"

n = int(input())

num1= n%60
num2=(n+1)%60

def fibonacci (n):
    a,b=0,1
    for i in range (2, n+1):
        c=a+b
        c=c%10
        b,a=c,b
    return c
if num1<=1:
    a=num1
else:
    a=fibonacci(num1)

if num2<=1:
    b=num2
else:
    b=fibonacci(num2)
    
print((a*b)%10)