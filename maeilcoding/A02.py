data = input()

# get first number of string
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    # add if zero or one
    if num <= 1 or result <= 1:
        result += num
    # multiply if not zero or one
    else:
        result *= num

print(result)