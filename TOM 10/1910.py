n = int(input())
powers = list(map(int, input().split()))

max_power, position = -1, 0
for i in range(1, n - 1):
    a = powers[i-1] +powers[i]+powers[i+1]
    if a > max_power:
        max_power = a
        position = i + 1

print(max_power, position, sep=" ")
