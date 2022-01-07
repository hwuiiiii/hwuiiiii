# binary search using if-else statement
def binary_search(array, target, start, end):
    while start <= end:
        middle = (start + end) // 2

        # return middle index if equal to target
        if array[middle] == target:
            return middle

        # check left side (move end point to left side) if target value is smaller than middle value
        elif array[middle] > target:
            end = middle - 1

        # check right side (move start point to right side) if target value is larger than middle value
        else:
            start = middle + 1

    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

print()