import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of adjacency relations
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# The minimal amount of steps required to completely propagate the advertisement
print("1")
