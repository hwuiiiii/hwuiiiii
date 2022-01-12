# memoization(caching) method
d = [0] * 100

# top-down dynamic programming - recursive function
def fibo(x):
    # terminate condition
    if x == 1 or x == 2:
        return 1
    # return if previously processed
    if d[x] != 0:
        return d[x]
    # return fibonacci result if not previously processed
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))