# 3차원 dp
# 0은 가로, 1은 세로, 2는 대각선

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1
for i in range(2,n):
    if board[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(n):
    print(dp[i])

for i in range(1, n):
    for j in range(2, n):
        if board[i][j] == 0:
            if board[i-1][j] + board[i][j-1] == 0: # 대각선에서 가져오려면 
                dp[i][j][2] = dp[i-1][j-1][2] + dp[i-1][j-1][1] + dp[i-1][j-1][0] # 대각선, 가로, 세로
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2] # 한 칸 위 대각선, 세로
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2] # 한 칸 옆 대각선, 가로
            

print(dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2])