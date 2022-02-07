# find set of x element
def find_parent(parent, x):
    # if not root node, find root node recursively
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union two sets
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# receive input
v, e = map(int, input().split())
parent = [0] * (v + 1)  # init parent table

# get list of all edges and their costs
edges = []
result = 0

# init parent table to self
for i in range(1, v + 1):
    parent[i] = i

# get all edge info
for _ in range(e):
    a, b, cost = map(int, input().split())
    # rearrange tuple so cost goes first (for sorting)
    edges.append((cost, a, b))

# sort edges by cost
edges.sort()

# check each edge
for edge in edges:
    cost, a, b = edge
    # include in set if not cycle
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)