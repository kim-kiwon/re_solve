#배열형 다익스트라
import heapq, sys

t = int(input())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

INF = sys.maxsize

for _ in range(t):
    n = int(input())
    data = []
    graph = [[INF] * (n) for _ in range(n)]
    for i in range(n):
        data.append(list(map(int, input().split())))
    graph[0][0] = data[0][0]
    q = []
    q.append((data[0][0], 0, 0))
    while q:
        dist, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                cost = dist + data[nx][ny]
                if graph[nx][ny] < cost:
                    continue
                graph[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(graph[n-1][n-1])


