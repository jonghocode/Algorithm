import sys
n = int(input())
lst = [0]*10010
for i in range(n):
    lst[i] = int(input())

dp = [0]*20010
dp[0], dp[1], dp[2] = lst[0], lst[0] + lst[1], max(dp[1], dp[0] + lst[2], lst[1] + lst[2])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i])

print(dp[n-1])