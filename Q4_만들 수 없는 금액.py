import sys
n = int(input())

data = list(map(int, input().split()))

data.sort()

sum_val = 0
for i in range(n):
    if sum_val + 1 < data[i]:
        print(sum_val + 1)
        sys.exit()
    sum_val += data[i]

print(sum_val + 1)