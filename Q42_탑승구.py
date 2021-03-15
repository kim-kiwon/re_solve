g = int(input())
p = int(input())

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

parent = [0] * (g+1)

for i in range(1, g+1):
    parent[i] = i

count = 0
for i in range(p):
    val = int(input())
    val_parent = find_parent(parent, val)
    if val_parent == 0:
        break
    union_parent(parent, val_parent, val_parent-1)
    count += 1

print(count)