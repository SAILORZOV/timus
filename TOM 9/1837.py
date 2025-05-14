from collections import deque


n = int(input())
teams = []
for _ in range(n):
    teams.append(input().split())


graph = {}

for team in teams:
    for person in team:
        if person not in graph:
            graph[person] = set()

    for i in range(len(team)):
        for j in range(len(team)):
            if i != j:
                graph[team[i]].add(team[j])


range_num = {}
queue = deque()
if "Isenbaev" in graph:
    queue.append((0, "Isenbaev"))

visited = set()

while queue:
    dist, person = queue.popleft()
    if person in visited:
        continue
    range_num[person] = dist
    visited.add(person)
    for i in graph[person]:
        if i not in visited:
            queue.append((dist + 1, i))

for i in graph:
    if i not in range_num:
        range_num[i] = "undefined"
sorted_keys = sorted(range_num.keys())
for i in sorted_keys:
    print(i, range_num[i])
