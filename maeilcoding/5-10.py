n, m = map(int, input().split())

# make 2 dim list
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# define dfs function : visit all linked nodes
def dfs(x, y):
    # end if exceeds set range
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # visit if node unvisited
    if graph[x][y] == 0:
        graph[x][y] = 1
        # dfs method to call N/S/W/F nodes
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# fill drink for all nodes
result = 0
for i in range(n):
    for j in range(m):
        # run dfs at current node
        if dfs(i, j) == True:
            result += 1

print(result)