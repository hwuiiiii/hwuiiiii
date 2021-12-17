from collections import deque

# define bfs method
def bfs(graph, start, visited):
    queue = deque([start])

    # current node visited
    visited[start] = True

    # continue until queue is empty
    while queue:
        # pop one node and print
        v = queue.popleft()
        print(v, end=' ')
        # append adjacent node(s) not visited to queue
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# make graph using list method
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# instantiate 1 dim list (corresponding to graph)
visited = [False] * 9

bfs(graph, 1, visited)
print()
