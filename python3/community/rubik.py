import math

n = int(input())
all = int(math.pow(n, 3))
inside = 0
if n - 1 > 0:
    inside = int(math.pow(n - 2, 3))
print(all - inside)
