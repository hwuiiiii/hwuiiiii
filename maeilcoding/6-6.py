array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# create list of array length (init with 0)
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1 # count for each number in array
  
for i in range(len(count)): # for each number in count list
  for j in range(count[i]): 
    print(i, end=" ") # print i element j times
  
print()