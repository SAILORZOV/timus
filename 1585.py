a = {'Emperor Penguin': 0, 'Little Penguin': 0, 'Macaroni Penguin': 0}

for i in range(int(input())):
    a[input()] += 1

print(max(a, key=a.get))