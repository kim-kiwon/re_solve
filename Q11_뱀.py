from collections import deque
n = int(input())
k = int(input())

direc = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = [[0] * (n) for _ in range(n)]
for i in range(k):
    x, y= map(int, input().split())
    arr[x-1][y-1] = 2

l = int(input())

moves = []
for i in range(l):
    x, c = input().split()
    moves.append((int(x), c))

hx, hy = 0, 0

def turn_snake(c): #방향에서 4로 나눈 나머지 취해주는 것에 유의. 이것때문에 인덱스초과 발생.
    global direc
    if c == 'D':
        direc = (direc + 1) % 4
    elif c == 'L':
        direc = (direc - 1) % 4

count = 0
idx = 0
snakes = deque()
snakes.append((0, 0))
while True:
    if count == moves[idx][0]:
        turn_snake(moves[idx][1])
        if idx < len(moves) - 1:
            idx += 1
    nhx, nhy = hx + dx[direc], hy + dy[direc]
    count += 1
    if nhx < 0 or nhx >= n or nhy < 0 or nhy >= n or ((nhx, nhy) in snakes):
        break
    elif arr[nhx][nhy] == 0: #이동 가능 & 사과 없으면 꼬리 당김
        snakes.popleft()
    else: #그 칸이 사과면
        arr[nhx][nhy] = 0
    snakes.append((nhx, nhy))
    hx, hy = nhx, nhy
print(count)