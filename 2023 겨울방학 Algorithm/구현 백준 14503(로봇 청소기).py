# 현재 칸이 청소되지 않았으면 청소
# 4방향 중 빈칸 없으면 후진, 벽이라 후진 할 수 없으면 작동 멈춤

# 반시계방향 90도 회전, 바라보는 방향 기준 앞쪽 청소 되지 않았으면 전진
# 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽

def turn(d):
    if d == 0:
        return 3
    else:
        return d - 1

def back(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1

n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
dirx, diry = [-1, 0, 1, 0], [0, 1, 0, -1]

while True:
    if board[x][y] == 0:
        visit[x][y] = 1

    flag = False
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visit[nx][ny] == 1 or board[nx][ny] == 1:
            continue
        flag = True

    if flag == False: # 청소할 칸이 없는 경우
        dir = back(d)
        nx, ny = x + dirx[dir], y + diry[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        if board[nx][ny] == 1:
            break
        x, y = nx, ny

    else: # 청소할 칸이 있으면
        for _ in range(4):
            d = turn(d)
            nx, ny = x + dirx[d], y + diry[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 1 or visit[nx][ny] == 1:
                continue
            x, y = nx, ny
            break

answer = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 1:
            answer += 1

print(answer)