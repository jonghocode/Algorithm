# 백준 16932(모양 만들기)
from collections import deque
def bfs(x, y, cnt):
    d = 1
    visit[x][y] = cnt
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dirx[i], y + diry[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visit[nx][ny] != 0 or board[nx][ny] == 0:
                continue
            q.append([nx, ny])
            visit[nx][ny] = cnt
            d += 1
    return d

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
dict = {}
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visit[i][j] == 0:
            temp = bfs(i, j, cnt)
            dict[cnt] = temp
            cnt += 1

answer = -1
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            tempchk = set()
            tempanswer = 1
            for k in range(4):
                ni, nj = i + dirx[k], j + diry[k]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                if visit[ni][nj] in tempchk or board[ni][nj] == 0:
                    continue
                tempchk.add(visit[ni][nj])
                tempanswer += dict[visit[ni][nj]]
            answer = max(answer, tempanswer)

print(answer)