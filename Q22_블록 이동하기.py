#BFS문제. 회전과 이동 가능한 경우 -> 큐와 방문에 삽입.
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

from collections import deque

def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    length = len(board)
    q = deque()
    q.append(((0, 0), (0, 1), 0))
    visited = []
    visited.append({(0, 0), (0, 1)}) #차지하는 두칸의 좌표 집합형태로 visited에 삽입.
    while q:
        #네방향 이동.
        now1, now2, count = q.popleft()
        if (now1[0], now1[1]) == (length-1, length-1) or (now2[0], now2[1]) == (length-1, length-1):
            return count
        for i in range(4):
            nx1 = now1[0] + dx[i]
            nx2 = now2[0] + dx[i]
            ny1 = now1[1] + dy[i]
            ny2 = now2[1] + dy[i]
            if 0<= nx1 < length and 0 <= nx2 < length and 0 <= ny1 < length and 0 <= ny2 < length:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    if {(nx1, ny1), (nx2, ny2)} not in visited:
                        visited.append({(nx1, ny1), (nx2, ny2)})
                        q.append(((nx1, ny1), (nx2, ny2), count + 1))
        #회전
        if now1[0] == now2[0] : #가로로 놓여져 있었으면
            if now1[0] - 1 >= 0:
                if board[now1[0] - 1][now1[1]] == 0 and board[now2[0] - 1][now2[1]] == 0: #위쪽으로 회전가능
                    if {now1, (now1[0] - 1, now1[1])} not in visited: #왼쪽위로 회전가능
                        visited.append({now1, (now1[0] - 1, now1[1])})
                        q.append((now1, (now1[0] - 1, now1[1]), count + 1))
                    if {now2, (now2[0] - 1, now2[1])} not in visited: #오른쪽위로 회전가능
                        visited.append({now2, (now2[0] - 1, now2[1])})
                        q.append((now2, (now2[0] - 1, now2[1]), count + 1))
            if now1[0] + 1 < length:
                if board[now1[0] + 1][now1[1]] == 0 and board[now2[0] + 1][now2[1]] == 0: #아래쪽으로 회전가능
                    if {now1, (now1[0] + 1, now1[1])} not in visited: #왼쪽아래로 회전가능
                        visited.append({now1, (now1[0] + 1, now1[1])})
                        q.append((now1, (now1[0] + 1, now1[1]), count + 1))
                    if {now2, (now2[0] + 1, now2[1])} not in visited: #오른쪽아래로 회전가능
                        visited.append({now2, (now2[0] + 1, now2[1])})
                        q.append((now2, (now2[0] + 1, now2[1]), count + 1))
        else: #세로로 놓여져 있으면
            if now1[1] - 1 >= 0:
                if board[now1[0]][now1[1] - 1] == 0 and board[now2[0]][now2[1] - 1] == 0: #왼쪽으로 회전가능
                    if {now1, (now1[0], now1[1] - 1)} not in visited: #왼쪽 위로 회전가능
                        visited.append({now1, (now1[0], now1[1] - 1)})
                        q.append((now1, (now1[0], now1[1] - 1), count + 1))
                    if {now2, (now2[0], now2[1] - 1)} not in visited: #왼쪽 아래로 회전가능
                        visited.append({now2, (now2[0], now2[1] - 1)})
                        q.append((now2, (now2[0], now2[1] - 1), count + 1))
            if now1[1] + 1 < length:
                if board[now1[0]][now1[1] + 1] == 0 and board[now2[0]][now2[1] + 1] == 0: #오른쪽으로 회전가능
                    if {now1, (now1[0], now1[1] + 1)} not in visited: #오른쪽 위로 회전가능
                        visited.append({now1, (now1[0], now1[1] + 1)})
                        q.append((now1, (now1[0], now1[1] + 1), count + 1))
                    if {now2, (now2[0], now2[1] + 1)} not in visited: #오른쪽 아래로 회전가능
                        visited.append({now2, (now2[0], now2[1] + 1)})
                        q.append((now2, (now2[0], now2[1] + 1), count + 1))


print(solution(board))