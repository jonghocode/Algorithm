# 1,1부터 시작 n,m 도착
# T시간 안에(T시간 이하)
# 그람을 찾는다면 벽 부수고 이동하기 가능
# 둘다 3차원 배열
import sys
from collections import deque

n, m, t = map(int, input().split())

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
chk = [[[10100 for _ in range(m)] for _ in range(n)] for _ in range(2)]
dirx, diry = [-1, 1, 0 ,0], [0, 0, -1, 1]
q = deque()
q.append([0, 0, 0])
chk[0][0][0] = 0

while q:
    x, y, sw = q.popleft()
    
    if board[x][y] == 2: # 검을 주웠다면
        sw = 1

    if x == n or y == m:
        break
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위를 벗어나면
            continue
        if chk[sw][nx][ny] != 10100: # 방문 했다면
            continue
        if sw == 0 and board[nx][ny] == 1: # 검을 들고있지 않은데 벽이라면
            continue
        if sw == 1:
            if chk[sw][x][y] == 10100:
                chk[sw][nx][ny] = chk[0][x][y] +1
            else:
                chk[sw][nx][ny] = chk[sw][x][y] + 1
        else :
            chk[sw][nx][ny] = chk[sw][x][y] + 1
        q.append([nx, ny, sw])


if t >= min(chk[0][n-1][m-1], chk[1][n-1][m-1]):
    print(min(chk[0][n-1][m-1], chk[1][n-1][m-1]))
else:
    print("Fail")