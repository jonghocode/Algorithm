import sys

n, k = map(int, input().split())
MAX = int(1e12)
board = [[MAX for _ in range(n+1)] for _ in range(n+1)]

for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1

for z in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] > board[i][z] + board[z][j]:
                board[i][j] = board[i][z] + board[z][j]

s = int(input())
for i in range(s):
    a, b = map(int, sys.stdin.readline().split())
    if board[a][b] == MAX:
        if board[b][a] != MAX:
            print(1)
        else:
            print(0)
    else:
        print(-1)