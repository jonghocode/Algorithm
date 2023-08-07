import sys

def dfs(x, y):
    if y == 9:
        x += 1; y = 0

    if x == 9:
        # 출력 후 프로그램 종료
        for i in range(9):
            for j in range(9):
                print(board[i][j],end='')
            print()
        sys.exit(0)

    if board[x][y] != 0:
        dfs(x, y+1)
    else:
        for i in range(1, 10):
            if r[x][i] == 0 and c[y][i] == 0 and rec[x//3*3 + y//3][i] == 0:
                board[x][y] = i
                r[x][i] = 1; c[y][i] = 1; rec[x//3*3 + y//3][i] = 1
                dfs(x, y+1)
                board[x][y] = 0
                r[x][i] = 0; c[y][i] = 0; rec[x//3*3 + y//3][i] = 0

# 9*9 입력받기
board = []
for i in range(9):
    board.append(list(map(int, input())))
# 행 체크, 열 체크, 3*3체크 배열
r = [[0]*10 for _ in range(10)]
c = [[0]*10 for _ in range(10)]
rec = [[0]*10 for _ in range(10)]

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            r[i][board[i][j]] = 1
            c[j][board[i][j]] = 1
            rec[i//3*3 + j//3][board[i][j]] = 1

dfs(0, 0)