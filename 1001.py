import math
import sys

numbers = sys.stdin.read().split()
for i in range(len(numbers)):
    numbers[i] = math.sqrt(int(numbers[i]))
numbers.reverse()
for i in numbers:
    print(i)
