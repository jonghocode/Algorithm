import sys

def dfs(x, y):

    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny] <= board[x][y]:
            continue
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    
    return dp[x][y]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
dp = [[-1 for _ in range(n)] for _ in range(n)]
answer = -1

for i in range(n):
    for j in range(n):
        dp[i][j] = dfs(i, j)
        answer = max(answer, dp[i][j])

print(answer)