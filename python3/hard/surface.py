import copy

l = int(input())
h = int(input())


def get_neighbours(x, y, the_map):
    neighbours = []
    if y - 1 >= 0 and the_map[y - 1][x] == 'O':
        the_map[y - 1][x] = 'X'
        neighbours.append([x, y - 1])
    if y + 1 < h and the_map[y + 1][x] == 'O':
        the_map[y + 1][x] = 'X'
        neighbours.append([x, y + 1])
    if x - 1 >= 0 and the_map[y][x - 1] == 'O':
        the_map[y][x - 1] = 'X'
        neighbours.append([x - 1, y])
    if x + 1 < l and the_map[y][x + 1] == 'O':
        the_map[y][x + 1] = 'X'
        neighbours.append([x + 1, y])
    return neighbours


lake_map = []
for i in range(h):
    row = list(input())
    lake_map.append(row)

n = int(input())

previous_checks = []
for i in range(n):
    temp_map = copy.copy(lake_map)
    x, y = [int(j) for j in input().split()]
    if temp_map[y][x] == '#':
        print('0')
    else:
        result = 0
        for check in previous_checks:
            if [x, y] in check:
                result = len(check)
                break
        if result == 0:
            temp_map[y][x] = 'X'
            neighbours = [[x, y]]
            target_neighbours = []
            while len(neighbours) > 0:
                neighbour = neighbours.pop(0)
                target_neighbours.append(neighbour)
                neighbours = neighbours + \
                    get_neighbours(neighbour[0], neighbour[1], temp_map)
                result = len(target_neighbours)
            previous_checks.append(target_neighbours)
        print(result)
