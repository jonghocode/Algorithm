import sys
input = sys.stdin.readline

n, m, t, d = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
MAX = int(1e12)
chk = [[0 for _ in range(m)] for _ in range(n)]
dis = [MAX for _ in range(n*m+1)]; dis[1] = 0
graph = []
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]

cnt = 1
for i in range(n):
    for j in range(m):
        chk[i][j] = cnt
        cnt += 1

for i in range(n):
    for j in range(m):
        if 'A' <= board[i][j] <= 'Z':
            board[i][j] = ord(board[i][j]) - ord('A')
        else:
            board[i][j] = ord(board[i][j]) - ord('A') - 6

for i in range(n):
    for j in range(m):
        if i == j:
            chk[i][j] = 0

for i in range(n):
    for j in range(m):
        for k in range(4):
            x, y = i + dirx[k], j + diry[k]
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            time = abs(board[i][j] - board[x][y])
            if time > t:
                continue
            if board[i][j] >= board[x][y]:
                chk[x][y] = 1
            else:
                chk[x][y] = time**2

for k in range(n):
    for i in range(n):
        for j in range(m):
            chk[i][j] = min(chk[i][j], chk[i][k] + chk[k][j])

print(dis)

for i in range(n):
    print(board[i])
for i in range(n):
    print(chk[i])

answer = 0
for i in range(n):
    for j in range(n):
        if chk[0][j] == MAX or chk[j][0] == MAX:
            continue
        if i == j:
            continue
        if chk[i][j] + chk[j][i] <= d and answer < board[i][j]:
            answer = board[i][j]

print(answer)