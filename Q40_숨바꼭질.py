import sys, heapq

n, m = map(int, input().split())

INF = sys.maxsize

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))

q = []
distance = [INF] * (n+1)
distance[1] = 0
q.append((0, 1))

while q:
    dist, now = heapq.heappop(q)
    for i in graph[now]:
        cost = dist + i[0]
        if distance[i[1]] > cost:
            distance[i[1]] = cost
            heapq.heappush(q, (cost, i[1]))

result = []
max_val = -sys.maxsize
max_node = 0
count = 0
for i in range(n, 0, -1):
    val = distance[i]
    if val != INF:
        max_val = max(max_val, val)
    if max_val == val:
        result.append(i)
        max_node = i
    else:
        count = 0

print(min(result), max_val, len(result))


