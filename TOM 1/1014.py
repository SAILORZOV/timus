import sys


def find_divider(num):
    for i in range(9, 1, -1):
        if num % i == 0:
            return str(i)
    return -1

number = int(input())
if number == 1:
    print(1)
    sys.exit(0)
if number == 0:
    print(10)
    sys.exit(0)
nums = []
while number != 1:
    divider = find_divider(number)
    if divider == -1:
        print(-1)
        sys.exit(0)
    number /= int(divider)
    nums.append(divider)
nums.sort()
print("".join(nums))
