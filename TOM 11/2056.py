import sys

n = int(input())
marks = []

for i in range(n):
    marks.append(int(input()))
if 3 in marks:
    print("None")
    sys.exit(0)
if marks.count(5) == n:
    print("Named")
    sys.exit(0)
if sum(marks) / n < 4.5:
    print("Common")
    sys.exit(0)
print("High")
