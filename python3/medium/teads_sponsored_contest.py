
n = int(input())  # the number of adjacency relations
nodes_map = {}
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    # Add nodes and its neighbours to map
    if yi not in nodes_map.keys():
        nodes_map[yi] = set([xi])
    else:
        nodes_map[yi].add(xi)
    if xi not in nodes_map.keys():
        nodes_map[xi] = set([yi])
    else:
        nodes_map[xi].add(yi)

# Specify the number of neighbours for each node
links = {}
for key, value in nodes_map.items():
    links[key] = len(value)

steps = 0
while len(links) > 1:
    # Find leaves (nodes with one neighbour)
    leaves = [x for x in links.keys() if links[x] == 1]
    for leaf in leaves:
        # For each leaf find its neighbours
        neighbours = nodes_map[leaf]
        for neighbour in neighbours:
            # For each neighbour decrease the number of its neighbours, because
            # of leaf removal
            if neighbour in links:
                links[neighbour] -= 1
        # Remove leaf
        del links[leaf]
    steps += 1

print(steps)
