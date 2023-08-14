# 적록색약이 아닌사람, 적록색약인 사람(R,G는 같은거임)
from collections import deque

n = int(input())
board = []
test = [[0]*n for _ in range(n)]
zx, zy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    board.append(list(input()))

for i in range(n): # 적록색약 맵 만들기
    for j in range(n):
        if board[i][j] == 'G':
            test[i][j] = 'R'
        else:
            test[i][j] = board[i][j]

def bfs(i, j, what, t):
    q = deque()
    chk = [[0]*n for _ in range(n)]
    q.append([i, j])
    chk[i][j] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + zx[i], y + zy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >=n:
                continue
            if chk[nx][ny] == 1 or t[nx][ny] != what:
                continue
            q.append([nx, ny])
            t[nx][ny] = ' '

cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] != ' ':
            cnt += 1
            bfs(i, j, board[i][j], board)

print(cnt, end = ' ')
cnt = 0
for i in range(n):
    for j in range(n):
        if test[i][j] != ' ':
            cnt += 1
            bfs(i, j, test[i][j], test)

print(cnt)