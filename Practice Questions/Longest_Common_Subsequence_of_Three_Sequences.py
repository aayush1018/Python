# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:06:02 2024

@author: Aayush
"""
'''Longest Common Subsequence of Three sequences problem - Compute the max length of a common subsequence
of the three sequences.
Input: Three seuqences. Output: The max length of a common subsequence '''

def longest_common_subsequence(seq1, seq2, seq3):
    len1, len2, len3 = len(seq1) , len(seq2), len(seq3)
    
    dp= [[[0]*(len3+1)for i in range(len2+1)]for i in range(len1+1)]
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            for k in range(1, len3+1):
                if seq1[i-1]==seq2[j-1]==seq3[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1]+1
                else:
                    dp [i][j][k]= max (dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    return dp[len1][len2][len3]

if __name__ == "__main__":
    n=int(input())
    seq1=list(map(int,input().strip().split()))
    
    m= int(input())
    seq2=list(map(int, input().strip().split()))
    
    l = int(input())
    seq3= list(map(int,input().strip().split()))
    
    result= longest_common_subsequence(seq1, seq2, seq3)
    print(result)