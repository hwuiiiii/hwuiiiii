import sys
input = sys.stdin.readline
INF = int(1e9)  # set infinity value

# read node and edge info
n, m = map(int, input().split())
# get start node
start = int(input())

# create list of node connection info
graph = [[] for i in range(n + 1)]

# create list tracking visited nodes
visited = [False] * (n + 1)

# initialize shortest distance table
distance = [INF] * (n + 1)

# get all edge info
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# get shortest distance node number amongst unvisited nodes
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # init on start node
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    # repeat for all n - 1 nodes excluding start node
    for i in range(n - 1):
        # get current shortest distance node and mark visited
        now = get_smallest_node()
        visited[now] = True

        # get nodes connected to current node
        for j in graph[now]:
            cost = distance[now] + j[1]

            # if passing current node is shorter than current cost
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# print all nodes
for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])