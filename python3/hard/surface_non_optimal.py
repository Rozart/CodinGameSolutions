import sys

l = int(input())
h = int(input())


def print_map(map):
    for y in range(0, len(map)):
        print(" ".join(map[y], file=sys.stderr))


def replace_in_map(source, target, map):
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            if map[y][x] == source:
                map[y][x] = target
    return map


def prepare_map(map):
    marker = 1
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            if map[y][x] == 'O':
                if y == 0:
                    if x - 1 >= 0 and map[y][x - 1] != '#':
                        map[y][x] = map[y][x - 1]
                    elif map[y][x] == 'O':
                        map[y][x] = str(marker)
                        marker += 1
                else:
                    if x - 1 >= 0 and map[y - 1][x] != '#' and map[y][x - 1] != '#':
                        map[y][x] = map[y - 1][x]
                        replace_in_map(map[y][x - 1], map[y - 1][x], map)
                    elif map[y - 1][x] != '#':
                        map[y][x] = map[y - 1][x]
                    elif x - 1 >= 0 and map[y][x - 1] != '#':
                        map[y][x] = map[y][x - 1]
                    else:
                        map[y][x] = str(marker)
                        marker += 1
    return map


def count_elements_at_point(x, y, map):
    element = map[y][x]
    counter = 0
    if element != '#':
        counter = sum(x.count(element) for x in map)
    return counter


map = []
for i in range(h):
    row = list(input())
    map.append(row)

map = prepare_map(map)
# print_map(map)

n = int(input())

for i in range(n):
    x, y = [int(j) for j in input().split()]
    print(count_elements_at_point(x, y, map))
