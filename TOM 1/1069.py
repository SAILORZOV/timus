import heapq


prufer = list(map(int, input().split()))

tree_len = max(len(prufer) + 1, max(prufer))

deg = [1] * (tree_len + 1)
for i in prufer:
    deg[i] += 1

edges = [[] for i in range(tree_len + 1)]


heap = []
for i in range(1, tree_len + 1):
    if deg[i] == 1:
        heapq.heappush(heap, i)

for u in prufer:
    v = heapq.heappop(heap)
    edges[u].append(v)
    edges[v].append(u)
    deg[u] -= 1
    deg[v] -= 1
    if deg[u] == 1:
        heapq.heappush(heap, u)


for i in range(1, tree_len + 1):
    print(f"{i}:", end='')
    for j in sorted(edges[i]):
        print(f" {j}", end='')
    print()