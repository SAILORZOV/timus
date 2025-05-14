num = int(input())

if num < 0:
    n = abs(num) + 2
elif num == 0:
    n = 2
else:
    n = num

print(int((num + 1) * n / 2))