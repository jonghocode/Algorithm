import sys
from collections import deque

n, k = map(int, input().split())
board = []
visit = [[-1 for _ in range(n)] for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque([])
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if board[i][j] != 0:
            q.append([i, j, 0, board[i][j]]) # 처음 큐에 들어갈 부분
            visit[i][j] = 0 # 방문 체크

s, ex, ey = map(int, input().split())

while q:
    x, y, d, t = q.popleft() # x좌표, y좌표, 깊이(시간), 현재 좌표 값 <- 처음에 이부분을 board[x][y]로 처리했다가 다른 전염되는 부분에도 바뀐값이 들어가서 따로 처리하는것으로 바꿨다.
    if d == s: # 깊이가 되면 종료
        break
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if (board[nx][ny] == 0 and visit[nx][ny] == -1) or (board[nx][ny] > t and visit[nx][ny] > d):
            # 한번도 방문하지 않았다면 전염시키고, 방문을 했던 곳(현재값보다 깊이가 커야함) 지금 값보다 크면 다시 넣기 
            board[nx][ny] = t
            visit[nx][ny] = d+1
            q.append([nx, ny, d+1, t])

print(board[ex-1][ey-1])