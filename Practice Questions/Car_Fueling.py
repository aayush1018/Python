# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:17:20 2024

@author: Aayush
"""

"Compute the minimum no of gas tank refills to get from one city to another"
"Input: Integers d and m, as well as a sequence of integers stop1<stop2<stopn"
"Output: The min no of refills to get from one city to another if a car can travel at most m miles on a full tank."
"The distance between the cities is d miles and there are gas stations at distances stop1, stop2, stopn along the way"
"Assume that a car starts with a full tank"

def min_refills(d, m, stops):
    # Add the destination distance as the last stop
    stops.append(d)
    
    count = 0  # Count of refills
    current_fuel = m  # Start with a full tank
    last_stop = 0  # Last stop position

    # Iterate through each stop
    for i in range(len(stops)):
        # Calculate the distance to the next stop
        required_fuel = stops[i] - last_stop
        
        # If the required fuel to reach the next stop is greater than the current fuel
        if required_fuel > current_fuel:
            count += 1  # Need to refill
            current_fuel = m  # Refill to full tank again

            # After refueling, check if we can reach the next stop
            if required_fuel > current_fuel:
                return -1  # Impossible to reach the next stop
        
        # Deduct the fuel used to reach this stop
        current_fuel -= required_fuel
        last_stop = stops[i]  # Update last stop position

    return count

# Example Input
if __name__ == "__main__":
    d = int(input())
    m = int(input())
    stops_len = int(input())
    stops = list(map(int, input().split()))

    # Calculate minimum refills
    result = min_refills(d, m, stops)
    print(result)