from collections import deque
board = [list(input()) for _ in range(8)]
# n-1,0 -> 0, n-1
# 모든 벽이 아래에 있는 행으로 한 칸씩 내려감
# 상,하,좌,우,대각선 이동 or 현재위치
# 캐릭터 먼저 이동, 벽 이동(두개가 만난다면 게임 끝)

q = deque([])
q.append([7, 0, 0])
dirx, diry = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1]
answer = 0
temp = [[['' for _ in range(8)] for _ in range(8)] for _ in range(12)]

for i in range(8):
    for j in range(8):
        temp[0][i][j] = board[i][j]

for k in range(1, 11):
    for i in range(7, 0, -1):
        for j in range(8):
            temp[k][i][j] = temp[k-1][i-1][j]
    for i in range(8):
        temp[k][0][i] = '.'

for k in range(1, 11):
    print(k)
    for i in range(8):
        for j in range(8):
            print(temp[k][i][j], end=' ')
        print()
    print()

while q:
    x, y, level = q.popleft()
    # print(x, y, level)
    people = [[0 for _ in range(8)] for _ in range(8)]
    if x == 0 and y == 7:
        answer = 1
        break
    
    for i in range(9):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
            continue
        if temp[level][nx][ny] == '#':
            continue
        
        people[nx][ny] = 1
    
    for i in range(8):
        for j in range(8):
            if people[i][j] == 1 and temp[level+1][i][j] == '.':
                q.append([i, j, level+1])



print(answer)

