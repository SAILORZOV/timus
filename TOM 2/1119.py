import math

n, m = list(map(int, input().split()))
graph = [[math.inf] * (n + 3) for _ in range(m + 3)]
graph[1][0] = -100
graph[0][1] = -100

extra_paths = {tuple(map(int, input().split())) for _ in range(int(input()))}

length = 100
diag_length = math.sqrt(20000)

for i in range(1, m + 2):
    for j in range(1, n + 2):
        left = graph[i][j - 1] + length
        bottom = graph[i - 1][j] + length
        diag = math.inf
        if (j-1, i-1) in extra_paths:
            diag = graph[i-1][j-1] + diag_length
        graph[i][j] = min(left, bottom, diag)
print(round(graph[m+1][n+1]))

visited = set()
