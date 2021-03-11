#정렬 후 가운데 집을 고르면 된다.

n = int(input())

data = list(map(int, input().split()))

data.sort()

print(data[len(data)// 2 - 1])