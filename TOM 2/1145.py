from collections import deque

n, m = list(map(int, input().split(" ")))

graph = []
for i in range(m):
    graph.append(list(input()))

good_cell = ()
flag = False
for i in range(1, m - 1):
    if flag:
        break

    for j in range(1, n - 1):
        if graph[i][j] == '.':
            good_cell = (i, j)
            flag = True
            break

visited = []
for i in range(m):
    visited.append([])
    for j in range(n):
        if graph[i][j] == "#":
            visited[i].append(True)
        else:
            visited[i].append(False)

longest_way = 0
farest_cell = ()


def search(start_x, start_y):
    visited = [[-1] * n for _ in range(m)]
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 0

    max_dist = 0
    max_cell = (start_x, start_y)

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == '.' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    if visited[nx][ny] > max_dist:
                        max_dist = visited[nx][ny]
                        max_cell = (nx, ny)
                    q.append((nx, ny))
    global farest_cell, longest_way
    farest_cell = max_cell
    longest_way = max_dist


search(good_cell[0], good_cell[1])

search(farest_cell[0], farest_cell[1])

print(longest_way)


