import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
total = c = int(input())
values = []
for i in range(n):
    b = int(input())
    values.append(b)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
result = []
if total > sum(values):
    print("IMPOSSIBLE");
else:
    values = sorted(values)
    for value in values:
        if value < total / n:
            result.append(value)
            n -= 1
            total -= value
        else:
            result.append(math.floor(total / n))

    result = sorted(result)
    diff = c - sum(result)

    i = 1
    while diff > 0:
        result[-i] += 1
        diff -= 1
        i+=1

for value in result:
    print(value)
