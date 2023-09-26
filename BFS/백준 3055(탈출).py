from collections import deque

r, c = map(int, input().split())
board = []
for i in range(r):
    board.append(list(map(str, input())))

# 초기값
waterst = []
zx, zy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if board[i][j] == 'D': # 비버 집
            ed = [i, j]
        elif board[i][j] == 'S': # 고슴도치 위치
            st = [i, j]
        elif board[i][j] == '*': # 물 위치
            waterst.append([i, j]) # 여러개가 있을 수 있음

water = [[0]*c for _ in range(r)]
water[st[0]][st[1]], water[ed[0]][ed[1]] = -1, -1

# 물을 먼저 퍼트리기
q = deque([])
for i, j in waterst: # 물 시작 값 넣기
    water[i][j] = 1
    q.append([i, j])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + zx[i], y + zy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c: # 범위를 벗어나면
            continue
        if water [nx][ny] == 0 and water[nx][ny] != -1 and board[nx][ny] == '.' and board[nx][ny] != 'X':
            q.append([nx, ny])
            water[nx][ny] = water[x][y] + 1

# 고슴도치 출발
go = [[0]*c for _ in range(r)]
go[st[0]][st[1]] = 1

q = deque([])
q.append([st[0], st[1]])

while q:
    x, y = q.popleft()
    if x == ed[0] and y == ed[1]:
        break
    for i in range(4):
        nx, ny = x + zx[i], y + zy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if (water[nx][ny] > go[x][y]+1 or board[nx][ny] == 'D' or water[nx][ny] == 0) and board[nx][ny] != 'X' and go[nx][ny] == 0:
            q.append([nx, ny])
            go[nx][ny] = go[x][y] + 1


for i in range(r):
    for j in range(c):
        print(water[i][j], end = ' ')
    print()
print()

for i in range(r):
    for j in range(c):
        print(go[i][j], end = ' ')
    print()

if go[ed[0]][ed[1]] == 0:
    print('KAKTUS')
else : print(go[ed[0]][ed[1]]-1)

# 5 5
# X*XXX
# .X...
# D....
# ...XS
# .....