def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print('type number of elements(int) and text(string) to search for using space as delimiter')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('type in full string text')
array = input().split()

print(sequential_search(n, target, array))