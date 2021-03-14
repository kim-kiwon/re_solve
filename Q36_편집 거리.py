src = input()
dest = input()

len_src = len(src)
len_dest = len(dest)

dp = [[0] * (len_dest + 1) for _ in range(len_src + 1)]

for i in range(len_src+1):
    dp[i][0] = i
for i in range(len_dest+1):
    dp[0][i] = i

for i in range(1, len_src + 1):
    for j in range(1, len_dest + 1):
        if src[i-1] != dest[j-1]:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        else:
            dp[i][j] = dp[i-1][j-1]
print(dp[len_src][len_dest])