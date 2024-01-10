from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque([(0, 0, 1)])
visit[0][0] = 1

while q:
    x, y, d = q.popleft()
    if x == n-1 and y == m-1:
        print(d)
        break
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == '0' or visit[nx][ny] == 1:
            continue
        q.append((nx, ny, d+1))
        visit[nx][ny] = 1