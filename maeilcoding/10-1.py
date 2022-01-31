# find parent of element
def find_parent(parent, x):
    # if not root node, search recursively until found
    if parent[x] != x:
        return find_parent(parent, parent[x])

    return x

# merge parents of each element
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# get number of nodes and edges(union count)
v, e = map(int, input().split())
parent = [0] * (v + 1)  # init parent table

# init parent nodes to self
for i in range(1, v + 1):
    parent[i] = i

# perform union calc
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('sets each element is in: ', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# print parent table content
print('parent table: ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end = ' ')

print()