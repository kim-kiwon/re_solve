from copy import deepcopy
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

check = [[1,2,3],[4,5,6],[7,8,9]]
def rotate_2d(key, num):
    temp = deepcopy(key)
    m = len(key)
    if num == 0:
        for i in range(m):
            for j in range(m):
                temp[i][j] = key[m-1-j][i]
    elif num == 1:
        for i in range(m):
            for j in range(m):
                temp[i][j] = key[m-1-i][m-1-j]
    elif num == 2:
        for i in range(m):
            for j in range(m):
                temp[i][j] = key[j][m-1-i]
    return temp

def check(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i+20][j+20] != 1:
                return False
    return True

def locker(lock, arr):
    n = len(lock)
    for i in range(n):
        for j in range(n):
            arr[i+20][j+20] = lock[i][j]

def solve(key, lock):
    arr = [[0] * 61 for _ in range(61)]
    n = len(lock)
    m = len(key)
    for turn in range(4):
        turn_key = rotate_2d(key, turn)
        for i in range(20-m+1, 20+n):
            for j in range(20-m+1, 20+n):
                locker(lock, arr)
                for a in range(m):
                    for b in range(m):
                        arr[i+a][j+b] += turn_key[a][b]
                if check(arr, n) == True:
                    return True
    return False

print(solve(key, lock))