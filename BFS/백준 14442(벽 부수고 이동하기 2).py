# 백준 14442(벽 부수고 이동하기 2)
from collections import deque
import sys
input = sys.stdin.readline

MAX = int(1e12)
n, m, k = map(int, input().split())
board = [0] + [[0] + list(input().strip()) for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
chk = [[[MAX for _ in range(m+1)] for _ in range(n+1)] for _ in range(k+1)]

q = deque()
q.append((1, 1, 0))
chk[0][1][1] = 1
answer = MAX
while q:
    x, y, cnt = q.popleft()
    
    if x == n and y == m:
        answer = min(answer, chk[cnt][x][y])
        continue

    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 1 or nx > n or ny < 1 or ny > m:
            continue
        if cnt < k and chk[cnt+1][nx][ny] > chk[cnt][x][y] + 1 and board[nx][ny] == '1': # 벽을 부수고 이동할 때
            chk[cnt+1][nx][ny] = chk[cnt][x][y] + 1
            q.append((nx, ny, cnt+1))
        elif chk[cnt][nx][ny] > chk[cnt][x][y] + 1 and board[nx][ny] == '0':
            chk[cnt][nx][ny] = chk[cnt][x][y] + 1
            q.append((nx, ny, cnt))

print(answer if answer != MAX else -1)