import sys
import math

n = int(input())
houses_y = []
min_x = None
max_x = None
for i in range(n):
    x, y = [int(j) for j in input().split()]
    houses_y.append(y)
    if min_x is None or x < min_x:
        min_x = x
    if max_x is None or x > max_x:
        max_x = x

houses_y = sorted(houses_y)
y_median = houses_y[n//2]

cable_length = abs(max_x - min_x)
for i in houses_y:
    cable_length += abs(y_median - i)

print(cable_length)
