import sys

input()
s = input().replace(" ", "")
print(s[:s.count("1")].count("0"))
