n = int(input())

# make dp table
d = [0] * 1001

# bottom-up dynamic programming
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])