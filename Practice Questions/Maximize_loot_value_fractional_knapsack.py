# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:22:41 2024

@author: Aayush
"""

"FInd the maximal value of items that fit into the backpack"
"Input: The capactiy of a backpack W as well as the weights (w1,wn) and costs (c1, cn) of n different compunds"
"Output: The maximum total value of fractions of items that fit into the backpack of the given capacity"

def fractional_knapsack (W, weights, costs):
    #creating a list of items as (value, weight) pairs
    items = [(costs[i], weights[i]) for i in range (len(weights))]
    #sorting item by value to weight ratio in descending order
    items.sort(key=lambda x:x[0] /x[1], reverse= True)
    
    total_value=0.0
    for value, weight in items:
        if W == 0:
            break
        if weight <=W:
            total_value += value #take the whole item
            W -= weight # decreasing the remaining capacity
        else:
            total_value += value * (W/weight) # traking the fraction of the item
            W=0 # backpack is now full
    return total_value

if __name__ == "__main__":
    n, W = map (int, input().split())
    weights = [] 
    costs = []
    for i in range (n):
        c, w = map (int, input().split())
        costs.append(c)
        weights.append(w)     
    max_value = fractional_knapsack(W, weights, costs)
    print(max_value)
    