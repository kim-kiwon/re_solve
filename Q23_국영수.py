n = int(input())

data = []
for i in range(n):
    name, k, e, m = input().split()
    k, e, m = int(k), int(e), int(m)
    data.append((name, k, e, m))

data.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(data[i][0])