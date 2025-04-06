lectures = []
count = 0
time = -1

n = int(input())
for i in range(n):
    lecture = list(map(int, input().split(' ')))
    lectures.append((lecture[1], lecture[0]))

lectures.sort()

for i in lectures:
    if i[1] > time:
        count += 1
        time = i[0]

print(count)
