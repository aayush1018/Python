# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 00:30:43 2024

@author: Aayush
"""

"Compute the last digit of the fibonacci numbers"
"Input: integers m<=n. Output: The last digit of the sum of the fib series"

m,n = [int(i) for i in input().split()]

if n<=1:
    print(n)
    quit()
    
num1 = (n+2)%60
num2 =(m+1)%60

def fibonacci(n):
    a,b=0,1
    for i in range (2, n+1):
        c=a+b
        c=c%10
        b,a=c,b
    return (c-1)
if num1<=1:
    a=num1-1
else:
    a=fibonacci(num1)
if num2<=1:
    b=num2-1
else:
    b=fibonacci(num2)
    
if a>=b:
    print(a-b)
else:
    print(10+a-b)
    