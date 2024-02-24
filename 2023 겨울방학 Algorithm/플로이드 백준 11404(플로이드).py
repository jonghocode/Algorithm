import sys

n = int(input())
m = int(input())
MAX = int(1e12)
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
board = [[MAX for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            board[i][j] = 0

for a, b, c in graph:
    if board[a][b] > c:
        board[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: continue
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(board[i][j], end=' ')
    print()