import sys

n, m, t, d = map(int, input().split())
board = []
MAX = int(1e12)
chk = [[MAX for _ in range(m)] for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
graph = [[MAX for _ in range(m*n+1)] for _ in range(n*m+1)]
for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if 'A' <= board[i][j] <= 'Z':
            board[i][j] = ord(board[i][j]) - ord('A')
        else:
            board[i][j] = ord(board[i][j]) - ord('A') - 6

cnt = 1
for i in range(n):
    for j in range(m):
        chk[i][j] = cnt
        cnt += 1

for i in range(n):
    for j in range(m):
        for k in range(4):
            if i == j:
                continue
            x, y = i + dirx[k], j + diry[k]
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if abs(board[i][j] - board[x][y]) < t:
                if board[i][j] >= board[x][y]: # 이동할 곳이 더 작거나 같다면
                    graph[chk[i][j]][chk[x][y]] = 1
                else:
                    graph[chk[i][j]][chk[x][y]] = (board[x][y] - board[i][j]) ** 2


for k in range(1, n*m+1):
    for i in range(1, n*m+1):
        for j in range(1, n*m+1):
            if i == j:
                continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

dict = {}
for i in range(n):
    for j in range(m):
        dict[chk[i][j]] = (i, j)

answer = 0
for i in range(1, n*m+1):
    if graph[1][i] == MAX or graph[i][1] == MAX:
        continue
    if graph[1][i] + graph[i][1] <= d and answer < board[(i-1)//m][(i-1)%m+1]:
        answer = board[(i-1)//m][(i-1)%m+1]
print(answer)