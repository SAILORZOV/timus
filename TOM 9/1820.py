import math

n, k = list(map(int, input().split()))

if n * 2 / k <= 1:
    print(2)
else:
    print(math.ceil(n * 2 / k))