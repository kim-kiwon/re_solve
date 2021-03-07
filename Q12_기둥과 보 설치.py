build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
n = 5
build_frame2 = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
def check(x, y, a, result):
    if a == 0:
        if [x, y-1, 0] in result or [x-1, y, 1] in result or [x,y,1] in result or y == 0:
            return True
        return False
    elif a == 1:
        if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
            return True
        return False


def solution(n, build_frame):
    result = []
    for data in bulid_frame:
        x, y, a, b = data
        if b == 1:
            if check(x, y, a, result):
                result.append([x, y, a])
        else:
            result.remove([x, y, a])
            for val in result:
                nx, ny, na = val
                if check(nx, ny, na, result) == False:
                    result.append([x, y, a])
                    break
    result.sort(key = lambda x : (x[0], x[1], x[2]))
    return result

print(solution(n, build_frame2))
