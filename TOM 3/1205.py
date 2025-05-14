import math
import heapq

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

walk_speed, metro_speed = map(float, input().split())
n = int(input())
stations = [list(map(float, input().split())) for _ in range(n)]

edges = [[] for _ in range(n + 2)]


while True:
    u, v = map(int, input().split())
    if u == v == 0:
        break
    u -= 1
    v -= 1
    d = dist(stations[u], stations[v]) / metro_speed
    edges[u].append((v, d))
    edges[v].append((u, d))


all_points = stations + [list(map(float, input().split())), list(map(float, input().split()))]
index_A = n
index_B = n + 1

for i in range(n + 2):
    for j in range(n + 2):
        if i == j:
            continue
        d = dist(all_points[i], all_points[j]) / walk_speed
        edges[i].append((j, d))

distances = [float('inf')] * (n + 2)
prev = [-1] * (n + 2)
distances[index_A] = 0

heap = [(0, index_A)]
while heap:
    curr_dist, u = heapq.heappop(heap)
    if curr_dist > distances[u]:
        continue
    for v, weight in edges[u]:
        if distances[v] > distances[u] + weight:
            distances[v] = distances[u] + weight
            prev[v] = u
            heapq.heappush(heap, (distances[v], v))


path = []
u = index_B
while u != -1:
    path.append(u)
    u = prev[u]
path.reverse()

print(f"{distances[index_B]:.7f}")

metro_path = []
for p in path:
    if p < n:
        metro_path.append(p + 1)

print(len(metro_path), end=" ")
for i in metro_path:
    print(i, end=" ")