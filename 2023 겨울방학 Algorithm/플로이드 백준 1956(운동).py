# chk가 되어있는데 또 갈려해 지금 값과 더한값이 사이클 합
import sys

n, m = map(int, input().split())
MAX = int(1e12)
board = [[MAX for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    board[a][b] = c

answer = MAX
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]
                answer = min(answer, board[i][j] + board[j][i])

print(-1 if answer == MAX else answer)