def recursive_function(i):

    if i == 100:
        return
    print(i, 'th recursive function', i+1, 'th function called')
    recursive_function(i + 1)
    print(i, 'exit function')

recursive_function(1)