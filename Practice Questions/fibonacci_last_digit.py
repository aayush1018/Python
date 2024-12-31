# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:03:11 2024

@author: Aayush
"""

"Compute the last digit of the n-th fibonacci number"
"Input: An integer n. Output: The last digit of the n-th Fibonacci number"

def fibonacci_last_digit(n):
    """Returns the last digit of the n-th Fibonacci number."""
    # Pisano period for modulo 10 is 60
    pisano_period = 60
    
    # Reduce n using Pisano period
    n = n % pisano_period
    
    if n == 0:
        return 0
    
    # Initialize the first two Fibonacci numbers
    previous, current = 0, 1
    
    # Compute Fibonacci numbers up to n modulo 10
    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10
    
    return current

# User input
n = int(input())

# Get the last digit of the n-th Fibonacci number
last_digit = fibonacci_last_digit(n)

print(last_digit)
