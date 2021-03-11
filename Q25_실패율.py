n = 4
stages = [2, 1, 2, 6, 2, 4, 3, 3]
stages2 = [4, 4, 4, 4, 4]

def solution(n, stages):
    result = [[i + 1] for i in range(n)]
    for i in range(n):
        result[i].append(stages.count(i+1))

    length = len(stages)

    for i in range(n):
        if length == 0:
            result[i].append(0)
        else:
            result[i].append(result[i][1] / length)
            length -= result[i][1]
    result.sort(key = lambda x : (-x[2], x[0]))
    result = [result[i][0] for i in range(n)]
    return result

print(solution(n, stages))