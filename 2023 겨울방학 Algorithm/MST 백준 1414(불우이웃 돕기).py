from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]
INF = 0x7fffffff
chk = [0 for _ in range(n)]
chk[0] = 1

for i in range(n):
    for j in range(n):
        if 'a' <= board[i][j] <= 'z':
            board[i][j] = ord(board[i][j])-ord('a')+1
        elif 'A' <= board[i][j] <= 'Z':
            board[i][j] = ord(board[i][j])-ord('A')+27
        else:
            board[i][j] = INF
temp = 0
for i in range(n):
    for j in range(n):
        if board[i][j] != INF:
            temp += board[i][j]

for i in range(n):
    for j in range(n):
        if i == j:
            board[i][j] = INF

for i in range(n):
    for j in range(n):
        if board[i][j] < board[j][i]:
            board[j][i] = board[i][j]
        else:
            board[i][j] = board[j][i]


q = deque()
q.append([0, 0])
cost = board[0]
while q:
    now, sum = q.popleft()

    MIN = INF
    for i in range(n):
        if chk[i] == 0 and cost[i] < MIN:
            MIN = cost[i]
            sw = i
    
    if MIN != INF:
        chk[sw] = 1
        q.append([sw, sum + MIN])
        for i in range(n):
            if chk[i] == 0 and board[sw][i] < cost[i]:
                cost[i] = board[sw][i]

for i in range(n):
    if chk[i] == 0:
        print(-1)
        exit()
print(temp - sum)