# 3차원 dp
# 0은 가로, 1은 세로, 2는 대각선

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

# for i in range(n): # 초기화
#     dp[0][i][0] = 1
dp[0][1][0] = 1
for i in range(2,n):
    if board[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(1, n):
    for j in range(2, n):
        if board[i][j] == 0:
            if board[i-1][j] + board[i][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][2] + dp[i-1][j-1][1] + dp[i-1][j-1][0]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            

# for i in range(n):
#     print(dp[i])
print(dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2])