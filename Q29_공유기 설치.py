import sys
n, c = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))

data.sort()

start = sys.maxsize
end = data[n-1] - data[0]
for i in range(1, n):
    start = min(data[i] - data[i-1], start)

answer = 0
while start <= end:
    mid = (start + end) // 2
    before = data[0]
    count = 1 #맨 처음위치에 공유기 설치함에 유의
    for i in range(1, n):
        now = data[i]
        gap = now - before
        if gap >= mid:
            before = now
            count += 1
    if count >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)