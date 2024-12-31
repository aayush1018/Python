# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:30:24 2024

@author: Aayush
"""

''' Maximum Amount of Gold Problem - Given a set of gold bars of various weights and a backpack that can hold
at most W pounds, place as much as gold as possible in the backpack.
Input: A set of n gold bars of integer weights w1, wn and a backpack that can hold at most W pounds
Output: A sebset of gold bars of maximum total weight not exceeding W '''

def knapsack (weights, W):
    n = len(weights)
    dp = [[0 for i in range (W+1)] for i in range(n+1)]
    
    #fill the dp table
    for i in range (1, n+1):
        for j in range(W+1):
            if weights[i-1] <=j:
                dp[i][j] = max (dp[i-1][j], dp[i-1][j-weights [i-1]] + weights[i-1])
            else:
                dp[i][j]=dp [i-1][j]
    return dp[n][W]

def main():
    W,n = map(int,input().split())
    weights = list(map(int, input().split()))
    
    max_weights= knapsack(weights, W)
    print(max_weights)
    
if __name__== "__main__":
    main()
    