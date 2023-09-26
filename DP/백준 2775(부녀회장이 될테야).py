n = int(input())
dp = [[0]*15 for _ in range(15)]

for i in range(15): # 0층 초기화
    dp[0][i] = i

for i in range(1, 15): 
    for j in range(1, 15):
        # 자신의 아래층 + 자신의 옆
        dp[i][j] = dp[i-1][j] + dp[i][j-1] 

for i in range(n):
    x = int(input())
    y = int(input())
    print(dp[x][y])