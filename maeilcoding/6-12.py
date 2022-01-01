n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # sort from smallest
b.sort(reverse=True) # sort from largest

# swap k times
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

    else:
        break

print(sum(a))