import heapq
n = int(input())

data = []
for i in range(n):
    heapq.heappush(data, int(input()))

sum_val = 0
while len(data) >= 2:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    sum_val += (a + b)
    heapq.heappush(data, a + b)

print(sum_val)

