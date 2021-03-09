from copy import deepcopy
n, m = map(int, input().split())
data = []
for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def virus(temp, x, y):
    if x < 0 or x >= n or y < 0 or y >= m or (temp[x][y] == 1 or temp[x][y] == 3):
        return
    temp[x][y] = 3
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        virus(temp, nx, ny)

def scoring(temp):
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count

score = 0
def solving(r, count):
    global score
    if count == 3:
        temp = deepcopy(data)
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(temp, i, j)
        score = max(score, scoring(temp))
        return
    for i in range(r, n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                solving(i, count + 1)
                data[i][j] = 0

solving(0, 0)
print(score)