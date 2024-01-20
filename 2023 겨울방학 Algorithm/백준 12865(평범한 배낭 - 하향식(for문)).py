import sys

n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(k+1)]

for w, v in lst:
    lst = list(dp)
    for i in range(w, k+1):
        dp[i] = max(dp[i], lst[i-w] + v)

print(max(dp))