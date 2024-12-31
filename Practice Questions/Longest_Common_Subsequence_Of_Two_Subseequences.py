# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:42:19 2024

@author: Aayush
"""

''' Longest Common SubSequence. COmpute the maximum length of a common subsequence of two sequences.
Input: Two sequences. Output: The Maximum length of a common subsequence '''

def longest_common_subsequence(seq1, seq2):
    m = len(seq1)
    n = len(seq2)
    
    #create a 2D array to store lengths of longest common subsequence
    dp = [[0]* (n+1) for i in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1]==seq2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 # characters match
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # take max of deleting one character
    return dp[m][n]

n = int(input().strip())
seq1= list(map(int,input().strip().split()))
m = int(input().strip())
seq2 = list(map(int, input().strip().split()))
length= longest_common_subsequence(seq1, seq2)
print(length)