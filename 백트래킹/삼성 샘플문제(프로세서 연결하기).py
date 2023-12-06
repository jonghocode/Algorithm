def back(d, cnt, n, p, success):
    global answer, answer2

    if d == cnt:
        sum = 0
        for i in range(n):
            for j in range(n):
                if visit[i][j] == 1:
                    sum += visit[i][j]
        if answer2 < success:
            answer = sum
            answer2 = success
        elif answer2 == success:
            if answer > sum:
                answer = sum
        return

    x, y = core[p][0], core[p][1]
    sw = 0
    for k in range(4):
        flag = False
        tx, ty = x, y
        while True: # 선을 이을 수 있다면
            nx, ny = tx + dirx[k], ty + diry[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                flag = True
                break
            if visit[nx][ny] == 1 or visit[nx][ny] == 2:
                break
            tx = nx; ty = ny
        if flag == True:
            sw = 1
            tx, ty = x, y
            while True:
                nx, ny = tx + dirx[k], ty + diry[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                tx = nx; ty = ny
                visit[tx][ty] = 1

            back(d+1, cnt, n, p+1, success+1)
            tx, ty = x, y
            while True:
                nx, ny = tx + dirx[k], ty + diry[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                tx = nx; ty = ny
                visit[tx][ty] = 0

    back(d+1, cnt, n, p+1, success)

t = int(input())
for q in range(t):
    n = int(input())
    board, core = [], []
    visit = [[0 for _ in range(n)] for _ in range(n)]
    dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
    chk = [0 for _ in range(n)]
    answer, answer2 = 0x7fffffff, -1
    for i in range(n):
        board.append(list(map(int, input().split())))
        for j in range(n):
            if board[i][j] == 1 and i != 0 and i != n-1 and j != 0 and j != n-1:
                core.append([i, j])
            if board[i][j] == 1:
                visit[i][j] = 2


    back(0, len(core), n, 0, 0)
    print(f"#{q+1} {answer}")