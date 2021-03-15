def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = find_parent(parent, a)
    else:
        parent[a] = find_parent(parent, b)

n, m = map(int, input().split())

graph = [[]for _ in range(n)]

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

data = []
for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)

for i in range(n):
    for j in range(n):
        if i != j and data[i][j] == 1:
            union_parent(parent, i, j)

course = list(map(int, input().split()))

can = 1

val = parent[course[0]]
for i in range(1, m):
    if parent[course[i]] != val:
        can = 0
        break

if can == 1:
    print("YES")
else:
    print("NO")