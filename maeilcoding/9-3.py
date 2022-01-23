INF = int(1e9)

# get node and edge input values
n = int(input())
m = int(input())

# make 2 dim list(graph) and initialize with INF
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# set self -> self to 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# set edge values
for _ in range(m):
    # a -> b with c cost
    a, b, c = map(int, input().split())
    graph[a][b] = c

# floyd-warshall algorithm
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# print results
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
print()