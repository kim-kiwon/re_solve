import sys

n = int(input())
m = int(input())

INF = sys.maxsize
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a][b] = min(graph[a][b], dist)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] != INF:
            print(graph[i][j], end = " ")
        else:
            print(0, end = " ")
    print()