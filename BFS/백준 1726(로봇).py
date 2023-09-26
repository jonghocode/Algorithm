import sys
from collections import deque

n, m = map(int, input().split())
board, chk = [], [[[0]*m for _ in range(n)] for _ in range(4)]
where = [[2, 3], [2, 3], [0, 1], [0, 1]] # 방향 좌표 -> 왼쪽 오른쪽으로 도는 경우
gox = [0, 0, 1, -1] # 동 서 남 북
goy = [-1, 1, 0, 0]
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

sx, sy, sz = map(int, input().split())
ex, ey, ez = map(int, input().split())
sx-=1; sy-=1; sz-=1; ez-=1; ey-=1; ez-=1

q = deque([])
q.append([sz, sx, sy])
chk[sz][sx][sy] = 1

while q:
    z, x, y = q.popleft()
    if x == ez and y == ey and z == ez:
        break

    # 앞으로 세 방향
    for i in range(1, 4):
        nx, ny = x + gox[z]*i, y + goy[z]*i

        if nx < 0 or nx >= n or ny < 0 or ny >= m : continue
        if board[nx][ny] == 1: break # 앞이 벽이라면

        if chk[z][nx][ny] == 0 and board[nx][ny] == 0:
            chk[z][nx][ny] = chk[z][x][y] + 1
            q.append([z, nx, ny])

    # 왼쪽 오른쪽
    if chk[where[z][0]][x][y] == 0:
        chk[where[z][0]][x][y] = chk[z][x][y] + 1
        q.append([where[z][0], x, y])
    
    if chk[where[z][1]][x][y] == 0:
        chk[where[z][1]][x][y] = chk[z][x][y] + 1
        q.append([where[z][1], x, y])

print(chk[ez][ex][ey]-1)