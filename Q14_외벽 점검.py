n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    for i in range(length): #모든 시작지점.
        start = weak[i]
        for friends in list(permutations(dist, len(dist))): #모든 dist 순열.
            count = 1
            max_val = start + friends[0]
            for idx in range(i, i + length): #현재 시작지점 + 순열 기준 count 계산
                if weak[idx] > max_val:
                    count += 1
                    if count > len(dist):
                        break
                    max_val = weak[idx] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    else:
        return answer

print(solving(n, weak, dist))