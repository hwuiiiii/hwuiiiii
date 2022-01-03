def binary_search(array, target, start, end):
    if start > end:
        return None
    middle = (start + end) // 2  # get middle index (drop decimal points)

    # if mid point equals target, return its index
    if array[middle] == target:
        return middle

    # redefine middle (switch end point to point before middle)
    elif array[middle] > target:
        return binary_search(array, target, start, middle - 1)

    # redefine middle (switch start point to point after middle)
    else:
        return binary_search(array, target, middle + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# print result and adjust for corner cases (ex. value does not exist in array)
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('Value does not exist.')
else:
    print(result + 1)