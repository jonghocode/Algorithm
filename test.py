from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]
INF = 0x7fffffff

for i in range(n):
    for j in range(n):
        if 'a' <= board[i][j] <= 'z':
            board[i][j] = ord(board[i][j]) - ord('a') + 1
        elif 'A' <= board[i][j] <= 'Z':
            board[i][j] = ord(board[i][j]) - ord('A') + 27
        else:
            board[i][j] = INF

line = 0
for i in range(n):
    for j in range(n):
        if board[i][j] != INF:
            line += board[i][j]

for i in range(n):
    for j in range(n):
        if i == j:
            board[i][j] = INF

for i in range(n):
    for j in range(n):
        M = min(board[i][j], board[j][i])
        board[i][j], board[j][i] = M, M


visit = [0 for _ in range(n)]
visit[0] = 1
cost = board[0]
q = deque()
q.append([0, 0])

while q:
    now, sum = q.popleft()
    M = INF

    for i in range(n):
        if visit[i] == 0 and cost[i] < M:
            M = cost[i]
            idx = i
    
    if M != INF:
        q.append([idx, sum + M])
        visit[idx] = 1

        for i in range(n):
            if visit[i] == 0 and cost[i] > board[idx][i]:
                cost[i] = board[idx][i]


for i in range(n):
    if visit[i] == 0:
        print(-1)
        exit()
print(line - sum)