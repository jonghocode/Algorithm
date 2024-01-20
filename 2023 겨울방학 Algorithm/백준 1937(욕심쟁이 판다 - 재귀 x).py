n = int(input())
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
dp = [[0 for _ in range(n)] for _ in range(n)]
board = [[0 for _ in range(n)] for _ in range(n)]
edge = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        edge.append((temp[j], i, j))
        board[i][j] = temp[j]

edge.sort()

answer = -1 
for cost, x, y in edge:
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if cost > board[nx][ny]:
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
    answer = max(answer, dp[x][y])

print(answer)
