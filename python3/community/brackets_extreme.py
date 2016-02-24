import sys

dict = {"}": "{", "]": "[", ")": "("}
stack = []
for i in input():
    if i in dict.values():
        stack.append(i)
    elif i in dict.keys() and stack[-1] == dict[i]:
        stack.pop()
print(str(len(stack) == 0).lower())
