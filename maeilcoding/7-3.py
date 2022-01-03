def binary_search(array, target, start, end):
    while start <= end:
        middle = (start + end) // 2

        # use if-else statement
        if array[middle] == target:
            return  middle

        elif array[middle] > target:
            end = middle - 1

        else:
            start = middle + 1

    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print('Value does not exist.')
else:
    print(result + 1)