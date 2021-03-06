n = input()

length = len(n)

left_sum = 0
right_sum = 0
for i in range(length):
    if i < length // 2:
        left_sum += int(n[i])
    else:
        right_sum += int(n[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")