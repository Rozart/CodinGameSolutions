import sys
import copy

l = int(input())
h = int(input())


def print_map(the_map):
    for y in range(0, len(the_map)):
        print(" ".join(the_map[y]), file=sys.stderr)


def get_neighbours(x, y, the_map):
    neighbours = []
    if the_map[y][x] == 'O':
        the_map[y][x] = 'X'
        if y - 1 >= 0 and the_map[y - 1][x] == 'O':
            neighbours.append([x, y - 1])
        if y + 1 < len(the_map) and the_map[y + 1][x] == 'O':
            neighbours.append([x, y + 1])
        if x - 1 >= 0 and the_map[y][x - 1] == 'O':
            neighbours.append([x - 1, y])
        if x + 1 < len(the_map[0]) and the_map[y][x + 1] == 'O':
            neighbours.append([x + 1, y])
    return neighbours


lake_map = []
for i in range(h):
    row = list(input())
    lake_map.append(row)

#map = prepare_map(map)

n = int(input())

for i in range(n):
    temp_map = copy.deepcopy(lake_map)
    x, y = [int(j) for j in input().split()]
    counter = 0
    neighbours = get_neighbours(x, y, temp_map)
    while len(neighbours) > 0:
        counter += 1
        neighbour = neighbours.pop(0)
        print(neighbour, file=sys.stderr)
        neighbours += get_neighbours(neighbour[0], neighbour[1], temp_map)
    print(counter)
