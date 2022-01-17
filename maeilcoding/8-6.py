n = int(input())
array = list(map(int, input().split()))

# create dp table
d = [0] * 100

# dynamic programming (bottom-up)
d[0] = array[0]  # first inventory
d[1] = max(array[0], array[1])  # check second inventory if larger than first

# choose inventory with max value
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# print final count in last inventory
print(d[n - 1])