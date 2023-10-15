# 상, 하, 좌, 우 이동
# 안전지대 반복 종료
# 우산있으면 우산 들기, 가지고있는 우산 버리고 새로운 우산
# 우산 -1 or 체력 -1
# 우산 0 되면 사라짐 or 체력 0 되면 죽음
# 체력이 남아있으면 반복

# 처음 S 위치에서 E 위치까지 우산 필요 없이 갈 수 있나? 체크
# 각 우산 마다 도착점 까지의 거리 계산
# 시작 지점에서 이동할 수 있는 우산만 넣기
# 그 우산에서 이동 가능한 곳만 넣기
# 그러다가 도착지점 만나면 종료

from collections import deque

n, h, d = map(int, input().split())
board = [list(input()) for i in range((n))]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'S':
            sx, sy = i, j
        elif board[i][j] == 'E':
            ex, ey = i, j

q = deque()
q.append([sx, sy, d, h, 0]) # 출발x, 출발y, 내구도, 체력, 깊이
while q:
    x, y, um, he, deep = q.popleft()
    if he == 0 and x == ex and y == ey: # 안전하게 탈출한다면
        print(deep)
        exit()
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue



print(-1) # 안전하게 탈출하지 못하면