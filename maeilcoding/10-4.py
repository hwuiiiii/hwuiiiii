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

# init parent table to self
for i in range(1, v + 1):
    parent[i] = i

cycle = False  # cycle yn

for i in range(e):
    a, b = map(int, input().split())
    # break if cycle
    if find_parent(parent, a) == find_parent(parent, b) :
        cycle = True
        break
    # union if sharing parent
    else:
        union_parent(parent, a, b)

if cycle:
    print("Cycle found.")
else:
    print("Cycle not found.")





