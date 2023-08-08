n, m, x, y, k = map(int, input().split())
board, zx, zy = [], [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0] # 위, 밑, 동, 서, 남, 북
move = [[0, 0, 0, 0, 0, 0], [3, 2, 0, 1, 4, 5], [2, 3, 1, 0, 4, 5], [4, 5, 2, 3, 1, 0], [5, 4, 2, 3, 0, 1]]

# test = dice[lst[0]]

for i in range(n):
    board.append(list(map(int, input().split())))

where = list(map(int, input().split()))

for i in where:
    nx = x + zx[i]; ny = y + zy[i]
    
    if nx < 0 or nx >=n or ny < 0 or ny >= m: continue

    # 주사위 이동
    test = []
    for j in range(6):
        test.append(dice[move[i][j]])

    if board[nx][ny] == 0:
        board[nx][ny] = test[1]

    elif board[nx][ny] != 0:
        test[1] = board[nx][ny]
        board[nx][ny] = 0
        # 쓰여있는 수가 바닥면에 복사되고 칸은 0
    x = nx; y = ny
    print(test[0])
    dice = test