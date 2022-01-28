INF = int(1e9)   # set infinity

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# set self -> self to 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# get all edge values and initialize
for _ in range(m):
    # set cost of a -> b and b -> a to 1
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# get passing node X and final node K
x, k = map(int, input().split())

# run fw algorithm
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# print results
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)