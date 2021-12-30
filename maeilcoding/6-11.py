n = int(input())

# save n students to list
array = []
for i in range(n):
    input_data = input().split()

    # save names as is(string), grades as int
    array.append((input_data[0], int(input_data[1])))

# get new sorted array (using lambda key, ascending)
array = sorted(array, key=lambda x: x[1])

# print result
for x in array:
    print(x[0], end=' ')

print()