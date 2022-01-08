n = int(input())
array = [0] * 1000001

# fill with 1 for all values that exist (n)
for i in  input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

# find if query values (m) are in array
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

print()