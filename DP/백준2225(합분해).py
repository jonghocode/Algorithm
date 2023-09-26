n, k = map(int, input().split())
dp = [[0]*(201) for _ in range(201)]
for i in range(1,n+1):
    dp[1][i] = 1

for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000

for i in range(n+1):
    for j in range(n+1):
        print(dp[i][j], end=' ')
    print()
print(dp[k][n])
