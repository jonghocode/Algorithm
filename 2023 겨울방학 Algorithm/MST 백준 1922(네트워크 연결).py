import sys
from collections import deque

n = int(input())
m = int(input())
INF = 0x7fffffff
board = [[INF for _ in range(n)] for _ in range(n)]
chk = [0 for _ in range(n)]
chk[0] = 1
q = deque()
q.append([0, 0])

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    board[a-1][b-1] = c
    board[b-1][a-1] = c
cost = board[0]

while q:
    now, sum = q.popleft()
    MIN = INF
    for i in range(n):
        if chk[i] == 0 and cost[i] < MIN:
            MIN = cost[i]
            sw = i

    if MIN != INF:
        q.append([sw, sum + MIN])
        chk[sw] = 1
        for i in range(n):
            if board[sw][i] < cost[i]:
                cost[i] = board[sw][i]

print(sum)