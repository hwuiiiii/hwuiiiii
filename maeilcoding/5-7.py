# adjacency list method : saves relations between connected nodes/edges only
graph = [[] for _ in range(3)]

# node 0 : (node, distance)
graph[0].append((1, 7))
graph[0].append((2, 5))

# node 1 : (node, distance)
graph[1].append((0, 7))

# node 2 : (node, distance)
graph[2].append((0, 5))

print(graph)