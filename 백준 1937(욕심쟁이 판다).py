import sys
sys.setrecursionlimit(10 ** 8)
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

zx, zy = [-1, 1, 0, 0], [0, 0, -1, 1]
dp = [[0]*n for _ in range(n)]
def dfs(x, y, dp):
    global n
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + zx[i], y + zy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[x][y] >= board[nx][ny]:
            continue
        dp[x][y] = max(dp[x][y], dfs(nx, ny, dp) + 1)
    return dp[x][y]

        
answer = -1
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j, dp))

print(answer)
