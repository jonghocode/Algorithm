# 산봉우리 구하기(8방향의 크기가 모두 같아야 함)
# main에서 2중 for문 돌면서 visit가 0 이면 들어간다. 현재 값을 가지고.
# 현재 값과 똑같은 값들만 큐에 넣기/ 8 방향 돌면서 한번이라도 주변에 큰 값이 있다면 break
# 시간 복잡도 : 큐에 들어갈 수 있는 경우의 수 -> O(n*m)

import sys
from collections import deque

def bfs(i, j, find):
    global answer
    chk = [[0 for _ in range(m)] for _ in range(n)]
    chk[i][j] = 1
    q = deque([])
    q.append([i, j])

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dirx[i], y + diry[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] > find:
                return
            if chk[nx][ny] == 1:
                continue
            if board[nx][ny] == find:
                q.append([nx, ny])
                chk[nx][ny] = 1
    
    for i in range(n):
        for j in range(m):
            if chk[i][j] == 1:
                visit[i][j] = 1

    answer += 1
    return

n, m = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
dirx, diry = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
answer = 0

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and board[i][j] != 0:
            bfs(i, j, board[i][j])

print(answer)