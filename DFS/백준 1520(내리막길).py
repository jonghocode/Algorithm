def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0

    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] >= board[x][y]:
            continue
        dp[x][y] += dfs(nx, ny)
    return dp[x][y]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]

dfs(0, 0)
print(dp[0][0])