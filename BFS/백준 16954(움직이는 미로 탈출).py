from collections import deque
board = [list(input()) for _ in range(8)]
# n-1,0 -> 0, n-1
# 모든 벽이 아래에 있는 행으로 한 칸씩 내려감
# 상,하,좌,우,대각선 이동 or 현재위치
# 캐릭터 먼저 이동, 벽 이동(두개가 만난다면 게임 끝)

# 1초 동안 욱제의 캐릭터가 먼저 이동하고, 그 다음 벽이 이동한다. 
# 벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없다.
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

while q:
    x, y, level = q.popleft()
    lst = []
    if level == 8:
        answer = 1
        break
    if x == 0 and y == 7:
        answer = 1
        break
    
    for i in range(9):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
            continue
        if temp[level][nx][ny] == '#':
            continue
        lst.append([nx, ny])
    
    for tx, ty in lst:
        if temp[level+1][tx][ty] == '.':
            q.append([tx, ty, level+1])
    

    # 만났는지 검사


print(answer)

