n = int(input())

data = list(map(int, input().split()))

data.sort()

count = 0

temp = []
for i in data:
    temp.append(i)
    if len(temp) >= i:
        temp = []
        count += 1

print(count)