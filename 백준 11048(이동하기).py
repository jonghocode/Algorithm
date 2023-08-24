n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + lst[i][j]

print(dp[n-1][m-1])