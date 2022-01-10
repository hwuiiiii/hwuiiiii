# get number of rice cakes(n) and requested amount(m)
n, m = list(map(int, input().split()))

# get all input lengths
array = list(map(int, input().split()))

# instantiate start and end points
start = 0
end = max(array)

# binary search using if-else statement
result = 0
while(start <= end):
    total = 0    # total count of rice cakes
    middle = (start + end) // 2
    for x in array:
        # get number of rice cakes after cut
        if x > middle:
            total += x - middle
    # if number of rice cakes is smaller than requested amount(m)
    if total < m :
        end = middle - 1
    # if number of rice cakes is enough search right side
    else:
        result = middle  # record middle point to result
        start = middle + 1

print(result)