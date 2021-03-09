#장애물 가능 위치를 combination으로 세개 정해서 풀 수도 있음
n = int(input())
data = []
teachers = []

for i in range(n):
    data.append(list(input().split()))
    for j in range(n):
        if data[i][j] == 'T':
            teachers.append((i, j))

result = False

def check():
    find = False
    for x, y in teachers:
        nx, ny = x, y
        if find == True:
            break
        while nx < n: #아래측 검사
            if data[nx][y] == 'O': break
            if data[nx][y] == 'S':
                find = True
                break
            nx += 1
        while ny < n: #우측 검사
            if data[x][ny] == 'O': break
            if data[x][ny] == 'S':
                find = True
                break
            ny += 1
        nx, ny = x, y
        while nx >= 0:
            if data[nx][y] == 'O': break
            if data[nx][y] == 'S':
                find = True
                break
            nx -= 1
        while ny >= 0:
            if data[x][ny] == 'O': break
            if data[x][ny] == 'S':
                find = True
                break
            ny -= 1
    return find

def solution(r, count):
    global result
    if count == 3:
        if check() == False:
            result = True
        return
    for i in range(r, n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O'
                solution(i, count + 1)
                data[i][j] = 'X'

solution(0, 0)
if result == True:
    print("YES")
else:
    print("NO")
