# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:09:33 2024

@author: Aayush
"""

"Compute the min num of coins needed to change the given value into coins with denominations 1,5,10"
"Input: An integer Money. Output: The min no of coins with denominations 1,5,10 that changes money"

def min_coins(change):
    #change value available
    change_value= [10,5,1]
    count =0
    for coin in change_value:
        if change>=coin:
            
            #calculate the number of coins in this denomination
            count+= change // coin
            #update the remaining value
            change %= coin
            
        if change == 0:
            break
        
    return count

if __name__ == "__main__":
    n = int(input())
    result = min_coins(n)
    print(result)