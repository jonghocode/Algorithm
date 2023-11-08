import sys
from collections import deque

# 30*12 * 200 * 200

k = int(input())
m, n = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chk = [[[0x7fffffff for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
hx, hy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]
dirx, diry = [-1, 1, 0, 0], [0, 0, 1, -1]

sx, sy, ex, ey = 0, 0, n-1, m-1
answer = 0x7fffffff
saved = -1

q = deque([])
q.append([sx, sy, 0, 0])
chk[0][sx][sy] = 1

while q:
    x, y, d, state = q.popleft()
    if x == ex and y == ey:
        answer = min(answer, d) # 나중에 들어온 값이 더 작을수도 있기 때문에
    
    if state < k: # 지금까지 이동한 횟수가 k보다 작다면 말처럼 이동
        for i in range(8):
            nx, ny = x + hx[i], y + hy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 1:
                continue
            if chk[state+1][nx][ny] > d + 1: # 체크되어있는 값이 이동할 값보다 크면
                chk[state+1][nx][ny] = d + 1
                q.append([nx, ny, d+1, state+1])
            
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 1:
            continue
        if chk[state][nx][ny] > d + 1: # 체크되어있는 값이 이동할 값보다 크면
            chk[state][nx][ny] = d + 1
            q.append([nx, ny, d+1, state])

if answer == 0x7fffffff:
    answer = -1
print(answer)