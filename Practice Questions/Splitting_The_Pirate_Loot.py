# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:13:23 2024

@author: Aayush
"""

''' Splitting the Pirate loot. Partition a set of integers into three subsets with equal sums
Input: A sequence of integers. Output: Check whether it is posible to partition them into three subsets
with equal sums i.e check whether there exists three disjoints sets'''

def can_partition (nums):
    total_sum = sum(nums)
    if total_sum % 3 != 0:
        return 0
    target = total_sum // 3
    n = len(nums)
    # Sort numbers in descending order for optimization
    nums.sort(reverse=True)
    # initialize the sums of three subsets 
    subsets= [0] * 3
    
    def backtrack(index):
        if index == n:
            return subsets [0] == subsets[1] ==subsets[2] ==target
        for i in range(3):
            if subsets[i] + nums[index] <=target:
                subsets[i] += nums[index]
                if backtrack (index +1):
                    return True
                subsets[i] -= nums[index]
            if subsets[i] == 0:
                break
        return False
    return 1 if backtrack(0) else 0

def main():
    n=int(input())
    nums=list(map(int,input().split()))
    results = can_partition(nums)
    print(results)
    
if __name__ == "__main__":
    main()
    