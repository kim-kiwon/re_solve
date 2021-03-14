n = int(input())
t, p = [], []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (n+1)
max_val = 0
for i in range(n-1, -1, -1):
    if i + t[i] <= n:
        dp[i] = max(dp[i + t[i]] + p[i], dp[i+1])
        max_val = dp[i]
    else:
        dp[i] = max_val

print(max(dp))