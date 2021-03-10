from collections import deque
n, l, r = map(int, input().split())

data = []
for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)

visited = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    global l, r
    unions = [(x, y)]
    sum_val = data[x][y]
    visited[x][y] = 1
    q = deque()
    q.append((data[x][y], x, y))
    while q:
        val, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    visited[nx][ny] = 1
                    unions.append((nx, ny))
                    sum_val += data[nx][ny]
                    q.append((data[nx][ny], nx, ny))
    if len(unions) == 1:
        return 0
    return (sum_val, unions)

count = 0
while True:
    visited = [[0] * n for _ in range(n)]
    result_val = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                result_tuple = bfs(i, j)
                if result_tuple != 0:
                    result_val.append(result_tuple)
    if len(result_val) == 0:
        break
    else:
        count += 1
        while result_val:
            sum_val, unions = result_val.pop()
            for x, y in unions:
                data[x][y] = sum_val // len(unions)

print(count)