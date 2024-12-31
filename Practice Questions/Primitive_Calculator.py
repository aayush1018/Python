# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:30:06 2024

@author: Aayush
"""
''' Primitive Calculator Problem
Find the min nuber of operations needed to get a positive integer n from 1 by using only 3 operations:
    add 1, multiply 2 and multiply 3. Input: An integer n. Output: The min num of operations needed to get n from 1 '''

from collections import deque

def min_operations_to_n(n):
    if n == 1:
        return 0, [1]
    
    queue = deque([1])  # Start from 1
    visited = {1: None}  # Track visited numbers and their predecessors

    while queue:
        current = queue.popleft()
        
        # Generate the next possible numbers with a preference for *3 and *2
        for next_num in (current * 3, current * 2, current + 1):  # Order changed
            if next_num > n:
                continue
            if next_num not in visited:
                visited[next_num] = current
                queue.append(next_num)
                
                # If we've reached n, we can stop
                if next_num == n:
                    # Reconstruct the path
                    path = []
                    while next_num is not None:
                        path.append(next_num)
                        next_num = visited[next_num]
                    path.reverse()
                    return len(path) - 1, path

# Example usage
n = int(input())  # Direct input for testing
k, sequence = min_operations_to_n(n)
print(k)
print(' '.join(map(str, sequence)))