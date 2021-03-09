from collections import deque
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (n+1)

q = deque()
q.append(x)
visited[x] = 0
while q:
    val = q.popleft()
    for i in graph[val]:
        if visited[i] == 0:
            visited[i] = visited[val] + 1
            q.append(i)

find = False
for i in range(1, n+1):
    if visited[i] == k:
        find = True
        print(i)

if find == False:
    print(-1)