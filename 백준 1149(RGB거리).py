import sys

n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().strip().split())))

# 위에서 밑으로 내려가면서 자신을 제외한 j중에서 더 작은 값으로 더하기

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1] + dp[i][0], dp[i-1][2] + dp[i][0])
    dp[i][1] = min(dp[i-1][0] + dp[i][1], dp[i-1][2] + dp[i][1])
    dp[i][2] = min(dp[i-1][0] + dp[i][2], dp[i-1][1] + dp[i][2])

print(min(dp[n-1]))
        