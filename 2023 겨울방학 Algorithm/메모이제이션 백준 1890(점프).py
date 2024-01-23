def dfs(x, y):
    if x == n-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    if y + board[x][y] < n:
        dp[x][y] += dfs(x, y + board[x][y])
    if x + board[x][y] < n:
        dp[x][y] += dfs(x + board[x][y], y)
    return dp[x][y]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
print(dfs(0, 0))