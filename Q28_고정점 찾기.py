n = int(input())

data = list(map(int, input().split()))

start = 0
end = len(data) - 1

find = False
while start <= end:
    mid = (start + end) // 2
    print(start, mid, end)
    if data[mid] == mid:
        find = True
        print(mid)
        break
    elif data[mid] >= mid:
        end = mid -1
    else:
        start = mid + 1

if find == False:
    print(-1)