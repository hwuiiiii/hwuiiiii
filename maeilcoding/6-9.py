array = [('banana', 2), ('apple', 5), ('carrot', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)

print(result)