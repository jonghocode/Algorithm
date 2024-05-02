import sys
input = sys.stdin.readline

def back(x, y, cnt, time):
    global answer

    if time > t:
        return
    answer = max(answer, cnt)
    for i in range(4):
        nx, ny = dirx[i] + x, diry[i] + y
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if chk[nx][ny] == 1:
            continue
        if board[nx][ny] == '#':
            continue
        if board[nx][ny] == 'S':
            chk[nx][ny] = 1
            back(nx, ny, cnt+1, time+1)
            chk[nx][ny] = 0
        if board[nx][ny] == '.':
            chk[nx][ny] = 1
            back(nx, ny, cnt, time+1)
            chk[nx][ny] = 0

n, m, t = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
chk = [[0 for _ in range(m)] for _ in range(n)]
dirx, diry = [-1, 1, 0, 0, 0], [0, 0, -1, 1, 0]
answer = -1

for i in range(n):
    for j in range(m):
        if board[i][j] == 'G':
            board[i][j] = '.'
            sx, sy = i, j

back(sx, sy, 0, 0)
print(answer)