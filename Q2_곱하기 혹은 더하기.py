s = list(input())

def check_val(a, b): #더하기가 좋으면 1을. 곱이 좋으면 0 반환
    if a == 0 or b == 0 or a == 1 or b == 1:
        return 1
    return 0

len_s = len(s)

result = int(s[0])
for i in range(len_s - 1):
    b = int(s[i + 1])
    if check_val(result, b) == 0:
        result *= b
    else:
        result += b

print(result)