def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

position = []
parent = [0] * n

for i in range(n):
    parent[i] = i

for i in range(n):
    x, y, z = map(int, input().split())
    position.append((x, y, z, i))

edges = []

for i in range(3):
    position.sort(key = lambda x : x[i])
    for j in range(1, n):
        dist = position[j][i] - position[j-1][i]
        now = position[j][3]
        prev = position[j-1][3]
        edges.append((dist, now, prev))

edges.sort()

result = 0
for edge in edges:
    dist, now, prev = edge
    if find_parent(parent, now) != find_parent(parent, prev):
        union_parent(parent, now, prev)
        result += dist

print(result)