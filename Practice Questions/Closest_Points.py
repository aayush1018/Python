# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:54:49 2024

@author: Aayush
"""

"closest Points"
''' Find the closest pair of points in a set of points on a plane.
Input: A list of n points on a plane
Output: The min distance between a pair of these points'''

import math

def distance_squared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def closest_pair_rec(points_sorted_x, points_sorted_y):
    if len(points_sorted_x) <= 3:
        min_dist = float('inf')
        for i in range(len(points_sorted_x)):
            for j in range(i + 1, len(points_sorted_x)):
                min_dist = min(min_dist, distance_squared(points_sorted_x[i], points_sorted_x[j]))
        return min_dist

    mid = len(points_sorted_x) // 2
    mid_point = points_sorted_x[mid]

    left_y = []
    right_y = []
    for point in points_sorted_y:
        if point[0] <= mid_point[0]:
            left_y.append(point)
        else:
            right_y.append(point)

    d1 = closest_pair_rec(points_sorted_x[:mid], left_y)
    d2 = closest_pair_rec(points_sorted_x[mid:], right_y)
    d = min(d1, d2)

    # Build the strip of points close to the line
    strip = [point for point in points_sorted_y if abs(point[0] - mid_point[0]) < math.sqrt(d)]
    
    # Efficiently check the points in the strip
    min_strip_dist = d
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1])**2 >= min_strip_dist:
                break  # No need to check further; points are too far apart in y-coordinates
            min_strip_dist = min(min_strip_dist, distance_squared(strip[i], strip[j]))

    return min(min_strip_dist, d)

def closest_pair(points):
    points_sorted_x = sorted(points, key=lambda p: p[0])
    points_sorted_y = sorted(points, key=lambda p: p[1])
    return closest_pair_rec(points_sorted_x, points_sorted_y)

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_distance_squared = closest_pair(points)
min_distance = math.sqrt(min_distance_squared)

print(min_distance)  # Format to 4 decimal places

    