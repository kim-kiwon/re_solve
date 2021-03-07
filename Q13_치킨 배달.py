import sys
from itertools import combinations

n, m = map(int, input().split())
arr = []
chickens = []
homes = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            chickens.append((i, j))
        elif temp[j] == 1:
            homes.append((i, j))

c_chickens = list(combinations(chickens, m))
f_result = sys.maxsize
for m_chicken in c_chickens:
    result = 0
    for home in homes:
        f_dist = sys.maxsize
        for i in range(m):
            dist = abs(home[0] - m_chicken[i][0]) + abs(home[1] - m_chicken[i][1])
            f_dist = min(dist, f_dist)
        result += f_dist
    f_result = min(f_result, result)

print(f_result)