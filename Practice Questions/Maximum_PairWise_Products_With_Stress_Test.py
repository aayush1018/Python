# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 23:10:24 2024

@author: Aayush

Maximum Pairwise Product
"""
"Define a method using the naive approach"
def max_pairwise_product (arr):
    max_product=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            max_product= max(max_product, arr[i]*arr[j])
    return max_product

"Define a method using fast approach"
def max_product_fast(arr):
    p1= max(arr)
    arr.remove(p1)
    p2=max(arr)
    return p1*p2

"Stress testing"
from random import randint
def max_product_stress_test(N,M):
    while True:
        n= randint(2,N)
        A = [None]*n
        for i in range(n):
            A[i]= randint(0,M)
        print(A)
        result1 = max_pairwise_product(A)
        result2 = max_product_fast(A)
        if result1==result2:
            print ("OK")
        else:
            print("Wrong answer: ", result1, result2)
            return 
        max_product_stress_test(5, 100)
        
   
"faster algorithm with the correct output for time complexity test cases"
def max_product_fast(arr):
    p1= max(arr)
    arr.remove(p1)
    p2=max(arr)
    return p1*p2

if __name__ == '__main__':
     _ = int(input())
     input_numbers = list(map(int, input().split()))
     print(max_product_fast(input_numbers))
