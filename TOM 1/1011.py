def floor(x):
    int_x = int(x)
    if x >= 0 or x == int_x:
        return int_x
    else:
        return int_x - 1

def ceil(x):
    int_x = int(x)
    if x <= 0 or x == int_x:
        return int_x
    else:
        return int_x + 1


P, Q = map(float, input().split())

n = 1
while True:
    if ceil(n * P / 100 + 0.00001) <= floor(n * Q / 100 - 0.00001):
        print(n)
        break
    n += 1
