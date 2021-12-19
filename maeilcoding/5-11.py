from collections import deque

n, m = map(int, input().split())

# 2 dim list
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# define four directions using dx, dy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# use bfs
def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    # repeat until queue is empty
    while queue:
        x, y = queue.popleft()

        # check all four directions
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # skip if out of bounds
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # skip if hits wall
            if graph[nx][ny] == 0:
                continue
            # visit if unvisited
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # return shortest path length
    return graph[n -1][m - 1]

print(bfs(0, 0))