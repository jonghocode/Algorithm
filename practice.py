from collections import deque

m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]
chk = [[0x7fffffff for _ in range(m)] for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]

q = deque()
q.append([0, 0])
chk[0][0] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if board[nx][ny] == '0' and chk[nx][ny] > chk[x][y]:
            chk[nx][ny] = chk[x][y]
            q.append([nx, ny])
        elif board[nx][ny] == '1' and chk[nx][ny] > chk[x][y] + 1:
            chk[nx][ny] = chk[x][y] + 1
            q.append([nx, ny])

print(chk[n-1][m-1])