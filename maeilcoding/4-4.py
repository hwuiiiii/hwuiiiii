n, m = map(int, input().split())

# initialize with zero
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1  # current x, y visited

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# NESW
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0

while True:

    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # unvisited after turning left
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # visited or sea after turning left
    else:
        turn_time += 1
    # all directions visited or sea
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # go back if possible
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # if sea is behine
        else:
            break
        turn_time = 0

print(count)
