a = input().split()
a[0] = int(a[0])
a[1] = len(a[1])

count = 1
while a[0] > 1:
    count *= a[0]
    a[0] -= a[1]
print(count)
