import sys

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    if x == n-1 and y == m-1:
        dp[x][y] = 1
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[x][y] <= board[nx][ny]:
            continue
        if dp[nx][ny] == 0:
            continue
        dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

n, m = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
dp = [[-1 for _ in range(m)] for _ in range(n)]
print(dfs(0, 0))
for i in range(n):
    print(dp[i])