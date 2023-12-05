# 공기청정기 항상 1번열, 2행 차지
# 1. 미세먼지 확산
# : 모든칸에서 동시에(큐에 넣어서 처리)
# : 4방향 확산
# : 4방향 중 공기청정기가 있거나 범위 벗어나거나 미세먼지 칸이라면
# : a[r][c] // 5만큼 확산
# : a[r][c]에 남은 양은 a[r][c] - (a[r][c]//5 * 방향개수)

# 2. 공기 청정기 작동
# : 위쪽은 반시계, 아래쪽은 시계
# : 바람이 불면 미세먼지가 한칸씩이동

from collections import deque

n, m, t = map(int, input().split())
clock, reclock, visit = [], [], [[0 for _ in range(m)] for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
board = []
q = deque()

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == -1:
            if len(reclock) == 0:
                reclock.append([i, j])
            else:
                clock.append([i, j])
        elif board[i][j] != 0:
            q.append([i, j, board[i][j]])

while t > 0:
    # 미세먼지 확산
    while q:
        x, y, k = q.popleft()
        cnt = 0
        for i in range(4):
            nx, ny = x + dirx[i], y + diry[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == -1:
                continue
            board[nx][ny] += k//5
            cnt += 1
        board[x][y] -= (k//5 * cnt)

    # 공기 청정기 작동(반시계)
    x, y = reclock[0][0]+1, reclock[0][1]+1
    temp = [[0 for _ in range(m)] for _ in range(n)]
    chk = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, x):
        temp[i][0] = board[i-1][0]
        chk[i][0] = 1
    for i in range(x-1):
        temp[i][m-1] = board[i+1][m-1]
        chk[i][m-1] = 1
    for i in range(m-1):
        temp[0][i] = board[0][i+1]
        chk[0][i] = 1
    for i in range(1, m):
        temp[x-1][i] = board[x-1][i-1]
        chk[x-1][i] = 1
    
    # 값 옮기기
    for i in range(n):
        for j in range(m):
            if chk[i][j] == 1 and board[i][j] != -1:
                if temp[i][j] == -1:
                    temp[i][j] = 0
                board[i][j] = temp[i][j]
    
    
    # 공기 청정기 작동(시계)
    x, y = clock[0][0], clock[0][1]
    temp = [[0 for _ in range(m)] for _ in range(n)]
    chk = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(x, n-1): # 0열
        temp[i][0] = board[i+1][0]
        chk[i][0] = 1
    for i in range(x+1, n): # 마지막 열
        temp[i][m-1] = board[i-1][m-1]
        chk[i][m-1] = 1
    for i in range(1, m): # 0행
        temp[x][i] = board[x][i-1]
        chk[x][i] = 1
    for i in range(m-1): # 마지막 행
        temp[n-1][i] = board[n-1][i+1]
        chk[n-1][i] = 1
    
    # 값 옮기기
    for i in range(n):
        for j in range(m):
            if chk[i][j] == 1 and board[i][j] != -1:
                if temp[i][j] == -1:
                    temp[i][j] = 0
                board[i][j] = temp[i][j]


    # q 초기화
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and board[i][j] != -1:
                q.append([i, j, board[i][j]])

    t -= 1

answer = 0
for i in range(n):
    for j in range(m):
        answer += board[i][j]

print(answer+2)