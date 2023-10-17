n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if board[i][j] != 0:
            board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j])+1

answer = -1
for i in board:
    answer = max(answer, max(i))
print(answer**2)