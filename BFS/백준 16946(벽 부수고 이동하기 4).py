from collections import deque

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visit[i][j] = 1
    temp = [[i, j]]
    d = 0
    while q:
        x, y = q.popleft()
        d+=1
        for k in range(4):
            nx, ny = x + dirx[k], y + diry[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny] == 1:
                continue
            if board[nx][ny] == 1:
                continue
            if visit[nx][ny] == 1:
                continue
            q.append([nx, ny])
            temp.append([nx, ny])
            visit[nx][ny] = 1

    for x, y in temp:
        visit[x][y] = d


n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]

Q = deque([])
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and board[i][j] == 0:
            bfs(i, j)
        if board[i][j] == 1:
            Q.append([i, j])

for i in range(n):
    for j in range(m):
        print(visit[i][j], end=' ')
    print()

while Q:
    x, y = Q.popleft()
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 0:
            visit[x][y] += visit[nx][ny]
        

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(board[i][j], end=' ')
        else:
            print(visit[i][j], end=' ')
    print()