from collections import deque

n = int(input())
walls = 0

cells = []
for i in range(n + 2):
    cells.append([])
cells[0] = list("#" * (n + 2))
cells[n + 1] = list("#" * (n + 2))
for i in range(n):
    cells[i + 1] = list(("#" + input() + "#"))

visited = set()
visited.add((1, 1))
visited.add((n, n))

queue = deque()
queue.append((1, 1))
queue.append((n, n))

while queue:
    cell = queue.popleft()
    if cells[cell[0] - 1][cell[1]] == "#":
        walls += 1
    elif (cells[cell[0] - 1][cell[1]] == ".") and ((cell[0] - 1, cell[1]) not in visited):
        queue.append((cell[0] - 1, cell[1]))
        visited.add((cell[0] - 1, cell[1]))

    if cells[cell[0] + 1][cell[1]] == "#":
        walls += 1
    elif (cells[cell[0] + 1][cell[1]] == ".") and ((cell[0] + 1, cell[1]) not in visited):
        queue.append((cell[0] + 1, cell[1]))
        visited.add((cell[0] + 1, cell[1]))

    if cells[cell[0]][cell[1] - 1] == "#":
        walls += 1
    elif (cells[cell[0]][cell[1] - 1] == ".") and ((cell[0], cell[1] - 1) not in visited):
        queue.append((cell[0], cell[1] - 1))
        visited.add((cell[0], cell[1] - 1))

    if cells[cell[0]][cell[1] + 1] == "#":
        walls += 1
    elif (cells[cell[0]][cell[1] + 1] == ".") and ((cell[0], cell[1] + 1) not in visited):
        queue.append((cell[0], cell[1] + 1))
        visited.add((cell[0], cell[1] + 1))




walls -= 4

print(walls * 9)
