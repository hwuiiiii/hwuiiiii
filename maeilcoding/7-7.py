n = int(input())
# make input set
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

# check if values in m exist in array
for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

print()