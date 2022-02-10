from collections import deque

# get input vertex, edge
v, e = map(int, input().split())
# set initial indegree to 0
indegree = [0] * (v + 1)
# init graph
graph = [[] for i in range(v + 1)]

# get edge input for directed graph
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # move from vertex a to vertex b
    # increase indegree by 1
    indegree[b] += 1

# define topology function
def topology_sort():
    result = []
    q = deque()

    # start with indegree 0 and insert into queue
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # repeat until queue is empty
    while q:
        now = q.popleft()
        result.append(now)
        # -1 on indegree for linked nodes
        for i in graph[now]:
            indegree[i] -= 1
            # insert into queue if indegree is 0
            if indegree[i] == 0:
                q.append(i)
    # print
    for i in result:
        print(i, end=' ')

topology_sort()

print()