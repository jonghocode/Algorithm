import sys
n = int(input())
k = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
zx, zy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서
stand = 1 # 처음 기준 1

for i in range(k):
    a, b = map(int,input().split())
    board[a][b] = 1


t = int(input())
headx, heady, time = 1, 1, 0
board[1][1] = 2
tail = [[1, 1]]
tcount = 0
apple, idx = [], 0

for i in range(t):
    # 입력 받은 값이랑 같을 때 까지 이동 후
    # 방향 전환 후 또 입력 받기
    apple.append(input().split(' '))


while True: # 이동
    nx = headx + zx[stand]
    ny = heady + zy[stand]
    time += 1
    if nx < 1 or nx > n or ny < 1 or ny > n or board[nx][ny] == 2:
        # 범위를 벗어나거나 자기자신과 만나면
        print(time, nx, ny, stand); sys.exit(0)

    if board[nx][ny] == 1: # 사과가 있다면
        board[nx][ny] = 2
    elif board[nx][ny] == 0:
        board[nx][ny] = 2
        if tcount < len(tail):
            board[tail[tcount][0]][tail[tcount][1]] = 0
            tcount += 1

    headx, heady = nx, ny
    tail.append([nx, ny])

    if idx < t and time >= int(apple[idx][0]):
        if apple[idx][1] == 'D':
            stand += 1
            if stand == 4:
                stand = 0
        elif apple[idx][1] == 'L':
            stand -= 1
            if stand == -1:
                stand = 3
        idx += 1
    print()
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(board[i][j], end = ' ')
        print()
    print(time)