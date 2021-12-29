n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

# sort by desc
array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')

print()