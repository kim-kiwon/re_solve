n = int(input())
result = []
result.append(1)

index_2, index_3, index_5 = 0, 0, 0
while True:
    if len(result) == n:
        break
    next_2 = result[index_2] * 2
    next_3 = result[index_3] * 3
    next_5 = result[index_5] * 5
    min_val = min(next_2, next_3, next_5)
    if min_val == next_2:
        index_2 += 1
    if min_val == next_3:
        index_3 += 1
    if min_val == next_5:
        index_5 += 1
    result.append(min_val)

print(result[n-1])