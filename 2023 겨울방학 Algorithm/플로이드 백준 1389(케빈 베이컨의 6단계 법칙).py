import sys

n, m = map(int, input().split())
MAX = int(1e12)
board = [[MAX for _ in range(n+1)] for _ in range(n+1)]
chk = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    chk[a][b] = 1
    chk[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if chk[a][b] and chk[a][k] and chk[k][b]:
                if board[a][b] > chk[a][k] + chk[k][b]:
                    board[a][b] = chk[a][k] + chk[k][b]

for i in range(1, n+1):
    print(board[i])