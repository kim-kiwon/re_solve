t = int(input())

for _ in range(t):
    n , m = map(int, input().split())
    data = [[0] * m for _ in range(n)]
    temp = list(map(int, input().split()))
    first_val = -1
    for i in range(len(temp)):
        a, b = divmod(i, m)
        data[a][b] = temp[i]
    for j in range(1, m):
        for i in range(n):
            if i - 1 >= 0 and i + 1 < n:
                data[i][j] = data[i][j] + max(data[i][j-1], data[i-1][j-1], data[i+1][j-1])
            elif i - 1 >= 0:
                data[i][j] = data[i][j] + max(data[i][j-1], data[i-1][j-1])
            elif i + 1 < n:
                data[i][j] = data[i][j] + max(data[i][j-1], data[i+1][j-1])
            else:
                data[i][j] = data[i][j] + data[i][j-1]
    max_val = 0
    for i in range(n):
        max_val = max(max_val, data[i][m-1])
    print(max_val)