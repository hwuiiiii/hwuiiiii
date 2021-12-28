array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # continue loop backwards(-1) starting from index i to 0
        if array[j] < array[j - 1]: # compare index with index on left side
            array[j], array[j - 1] = array[j - 1], array[j] # swap if index is smaller than index on left side
        else:
            break

print(array)
print()