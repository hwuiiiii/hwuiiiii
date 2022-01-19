n, m = map(int, input().split())

# save money value as array
array = []
for i in range(n):
    array.append(int(input()))

# make dp table (set 10001 as default value for nonexistent)
d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # if exists way to make (i - k) won
            d[j] = min(d[j], d[j - array[i]]+ 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])