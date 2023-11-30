# 행성 탐사
# 누적합
import sys

n, m = map(int, input().split())
k = int(input())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
search = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

chk = [[[0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(3)]

for i in range(1, n+1):
    for j in range(1, m+1):
        now = board[i-1][j-1]
        if now == 'J':
            chk[0][i][j] += 1
        elif now == 'O':
            chk[1][i][j] += 1
        elif now == 'I':
            chk[2][i][j] += 1
        chk[0][i][j] = chk[0][i-1][j] + chk[0][i][j-1] - chk[0][i-1][j-1] + chk[0][i][j]
        chk[1][i][j] = chk[1][i-1][j] + chk[1][i][j-1] - chk[1][i-1][j-1] + chk[1][i][j]
        chk[2][i][j] = chk[2][i-1][j] + chk[2][i][j-1] - chk[2][i-1][j-1] + chk[2][i][j]


for i in range(k):
    a, b, c, d = search[i][0], search[i][1], search[i][2], search[i][3]
    print(chk[0][c][d] - chk[0][a-1][d] - chk[0][c][b-1] + chk[0][a-1][b-1], end=' ')
    print(chk[1][c][d] - chk[1][a-1][d] - chk[1][c][b-1] + chk[1][a-1][b-1], end=' ')
    print(chk[2][c][d] - chk[2][a-1][d] - chk[2][c][b-1] + chk[2][a-1][b-1])
    
