from collections import deque

n, m = map(int, input().split())
board, chk = [], [[[0 for _ in range(m)] for _ in range(n)] for _ in range(65)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
dict = {'A' : 5, 'B' : 4, 'C' : 3, 'D' : 2, 'E' : 1, 'F' : 0, 'a' : 5, 'b' : 4, 'c' : 3, 'd' : 2, 'e' : 1, 'f' : 0,}
for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == '0':
            sx, sy = i, j

q = deque([(sx, sy, 0, 0)])
while q:
    x, y, num, d = q.popleft()
    if board[x][y] == '1': 
        print(d)
        exit()
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if board[nx][ny] == '#': continue
        if chk[num][nx][ny] == 1: continue
        if board[nx][ny] == '.' or board[nx][ny] == '0' or board[nx][ny] == '1':
            q.append((nx, ny, num, d+1))
            chk[num][nx][ny] = 1
        if 'A' <= board[nx][ny] <= 'F' and num & (1 << dict[board[nx][ny]]): # 열쇠를 가지고 있다면
            q.append((nx, ny, num, d+1))
            chk[num][nx][ny] = 1
        if 'a' <= board[nx][ny] <= 'f': # 열쇠라면 줍기
            t = num | (1 << dict[board[nx][ny]])
            q.append((nx, ny, t, d+1))
            chk[t][nx][ny] = 1

print(-1)