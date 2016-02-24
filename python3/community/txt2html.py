import sys

n = int(input())
table = []
row = []
s = input()
for i in range(1,n):
    s = input()
    if "+-" in s:
        table.append(row)
        row = []
    else:
        temp_row = list(filter(None,s.split("|")))
        if len(row) == 0:
            row = temp_row
        else:
            for index, x in enumerate(temp_row):
                row[index] = (row[index].strip() + " " + x.strip()).strip()

t="<table>\n"
for x in range(len(table)):
    t+="<tr>"
    for y in range(len(table[0])):
        t+="<td>"
        t+=table[x][y].strip()
        t+="</td>"
    t+="</tr>\n"
t+="</table>"
print(t.strip())
