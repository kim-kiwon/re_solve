s = ['2'] + list(input())

chunk_0 = 0
chunk_1 = 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            chunk_0 += 1
        else:
            chunk_1 +=1

print(min(chunk_0, chunk_1))