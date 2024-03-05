import sys
input = sys.stdin.readline

n, m, t, d = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
chk = [[0 for _ in range(m)] for _ in range(n)]
MAX = int(1e12)
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
        for k in range(4):
            x, y = i + dirx[k], j + diry[k]
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            time = abs(board[i][j] - board[x][y])
            if time > t:
                continue
            if board[i][j] >= board[x][y]:
                graph.append((chk[i][j], chk[x][y], 1))
            else:
                graph.append((chk[i][j], chk[x][y], time**2))

graph2 = []
answer = 0
for i in range(n):
    for temp in graph:
        a, b, c = temp
        if dis[a] == MAX:
            continue
        if dis[b] > dis[a] + c and dis[a] + c <= d:
            dis[b] = dis[a] + c
            graph2.append(a)
            graph2.append(b)

for k in graph2:
    for i in range(n):
        for j in range(m):
            if chk[i][j] == k:
                answer = max(answer, board[i][j])

print(dis)
print(answer)

for i in range(n):
    print(board[i])
for i in range(n):
    print(chk[i])
for i in graph:
    print(i)