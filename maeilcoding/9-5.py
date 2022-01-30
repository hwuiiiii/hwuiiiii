import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# get note count, edge count, start node
n, m, start = map(int, input().split())
# get list of all nodes and its edges
graph = [[] for _ in range(n + 1)]
# init shortest distance table values as INF
distance = [INF] * (n + 1)

# get all edge info
for _ in range(m):
    x, y, z = map(int, input().split())
    # cost z from x -> y
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # input start node and its cost to 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # if q is not empty
        # get info of shortest distance node
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # check all linked nodes for current(now) node
        for i in graph[now]:
            cost = dist + i[1]
            # if cost is lower when passing other nodes
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# count for reachable nodes
count = 0
max_distance = 0 # count for farthest node
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# print (-1 to exclude start node)
print(count - 1, max_distance)
