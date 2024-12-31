# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:16:30 2024

@author: Aayush
"""

'''Compute the edit distance between two strings
Input: Two Strings
Output: The min number of single - symbol insertions, deletions and substituions to tranform one string into the other one '''

def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a 2D array to store the edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the base cases
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting all characters from str1
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting all characters to match str2

    # Compute the edit distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,    # Deletion
                    dp[i][j - 1] + 1,    # Insertion
                    dp[i - 1][j - 1] + 1  # Substitution
                )

    return dp[m][n]

# Input format
str1 = input().strip()  # Read first string
str2 = input().strip()  # Read second string

# Calculate edit distance
distance = edit_distance(str1, str2)

# Output format
print(distance)
