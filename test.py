from collections import deque
import sys
input = sys.stdin.readline

def ice(board):
    sx, sy = -1, -1
    visit = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                sx, sy = i, j

    if sx == -1 and sy == -1:
        return True
    
    q = deque([(sx, sy)]); visit[sx][sy] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dirx[i], y + diry[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0 or visit[nx][ny] == 1:
                continue
            q.append((nx, ny))
            visit[nx][ny] = 1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and visit[i][j] != 1:
                return True
    
    return False

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0

while True:
    if ice(board):
        break
    
    answer += 1

    chk = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(4):
                x, y = i + dirx[k], j + diry[k]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if board[x][y] != 0:
                    continue
                cnt += 1
            chk[i][j] = cnt
    
    for i in range(n):
        for j in range(m):
            board[i][j] -= chk[i][j]
            if board[i][j] < 0:
                board[i][j] = 0

print(answer)