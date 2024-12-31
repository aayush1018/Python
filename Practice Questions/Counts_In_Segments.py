# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:34:00 2024

@author: Aayush
"""

''' Given a set of points and a set of segments on a line, compute, for each point, the number of segments it is contained in.
Input: A list of segments and a list of points
Output: The number of segments containing each point '''

master_list = list()
s, p = [int(i) for i in input().split()]

for i in range(s):
    a, b = [int(i) for i in input().split()]
    master_list.append((a,'l'))
    master_list.append((b,'r'))

points = input().split()
for i in points:
    master_list.append((int(i),'p'))

master_list.sort()

segment_count = 0
point_segment_map = dict()
for i in master_list:
    if i[1] == 'l': segment_count += 1
    elif i[1] == 'r': segment_count -= 1
    else:
        point_segment_map[i[0]] = segment_count

temp = ''
for i in points:
    temp += str(point_segment_map[int(i)]) + ' '
print(temp[:-1])
    