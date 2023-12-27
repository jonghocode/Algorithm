# 3차원 배열 이용

from collections import deque

m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]
chk = [[[0x7fffffff for _ in range(m)] for _ in range(n)] for _ in range(2)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]

q = deque()
q.append([0, 0])
chk[1][0][0], chk[0][0][0] = 0, 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == '1' and board[x][y] == '0' and chk[1][nx][ny] > chk[0][x][y] + 1:
            chk[1][nx][ny] = chk[0][x][y] + 1
            q.append([nx, ny])
        
        elif board[nx][ny] == '1' and board[x][y] == '1' and chk[1][nx][ny] > chk[1][x][y] + 1:
            chk[1][nx][ny] = chk[1][x][y] + 1
            q.append([nx, ny])

        elif board[nx][ny] == '0' and board[x][y] == '1' and chk[0][nx][ny] > chk[1][x][y]:
            chk[0][nx][ny] = chk[1][x][y]
            q.append([nx, ny])
        
        elif board[nx][ny] == '0' and board[x][y] == '0' and chk[0][nx][ny] > chk[0][x][y]:
            chk[0][nx][ny] = chk[0][x][y]
            q.append([nx, ny])

print(min(chk[0][n-1][m-1], chk[1][n-1][m-1]))




# 다익스트라

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