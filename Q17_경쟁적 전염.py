from collections import deque

n, k = map(int, input().split())

q = []
data = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0:
            q.append((temp[j], 0, i, j))
    data.append(temp)

s, destx, desty = map(int, input().split())

q.sort() #바이러스 작은 순대로 온다는 보장X. 정렬 필요.
q = deque(q)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
    val, time , x, y = q.popleft()
    if time >= s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < n and data[nx][ny] == 0:
            data[nx][ny] = val
            q.append((val, time+1, nx, ny))

print(data[destx-1][desty-1])