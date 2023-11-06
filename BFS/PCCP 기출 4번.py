from collections import deque

def solution(maze):
    answer = 0
    dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
    chk = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]for _ in range(4)]
    board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(2)]
    visit = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(2)]
    n = len(maze)
    m = len(maze[0])
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rsx, rsy = i, j
            elif maze[i][j] == 2:
                bsx, bsy = i, j
            elif maze[i][j] == 3:
                rex, rey = i, j
            elif maze[i][j] == 4:
                bex, bey = i, j
    
    rq = deque([])
    rq.append([rsx, rsy, 1])
    board[0][rsx][rsy] = 1
    while rq:
        x, y, d = rq.popleft()
        for i in range(4):
            nx, ny = x + dirx[i], y + diry[i]
            if nx < 0 or nx >= n or ny < 0 or ny>=m:
                continue
            if board[0][nx][ny] != 0:
                continue
            # if nx == rex and ny == rey:
            #     continue
            if maze[nx][ny] == 5:
                continue
            rq.append([nx, ny, d+1])
            board[0][nx][ny] = d+1
    
    bq = deque([])
    bq.append([bsx, bsy, 1])
    board[1][bsx][bsy] = 1
    while bq:
        x, y, d = bq.popleft()
        for i in range(4):
            nx, ny = x + dirx[i], y + diry[i]
            if nx < 0 or nx >= n or ny < 0 or ny>=m:
                continue
            if board[1][nx][ny] != 0:
                continue
            # if nx == bex and ny == bey:
            #     continue
            if maze[nx][ny] == 5:
                continue
            bq.append([nx, ny, d+1])
            board[1][nx][ny] = d+1
    visit[0][rsx][rsy] = 1
    visit[1][bsx][bsy] = 1
    q = deque([])
    q.append([rsx, rsy, bsx, bsy, 0, 0, 0])
    chk[rsx][rsy][bsx][bsy] = 1
    for i in range(n):
        for j in range(m):
            print(board[0][i][j], end=' ')
        print()
    print()
    for i in range(n):
        for j in range(m):
            print(board[1][i][j], end=' ')
        print()
    print()
    
    while q:
        rx, ry, bx, by, d, rstate, bstate = q.popleft()
        print(rx, ry, bx, by, d, rstate, bstate)
        
        if rstate == 1 and bstate == 1:
            answer = d
            break
        if rstate == 1:
            for i in range(4):
                sw = 0
                nx, ny = bx + dirx[i], by + diry[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if maze[nx][ny] == 5:
                    continue
                if chk[rx][ry][nx][ny] == 1:
                    continue
                if nx == rex and ny == rey: #!
                    continue
                if visit[0][nx][ny] == 1:
                    continue
                if nx == bex and ny == bey:
                    sw = 1
                q.append([rx, ry, nx, ny, d+1, 1, sw])
                chk[rx][ry][nx][ny] = 1
                visit[0][nx][ny] = 1
        elif bstate == 1:
            for i in range(4):
                sw = 0
                nx, ny = rx + dirx[i], ry + diry[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if maze[nx][ny] == 5:
                    continue
                if chk[nx][ny][bx][by] == 1:
                    continue
                if nx == bex and ny == bey: #!
                    continue
                if visit[1][nx][ny] == 1:
                    continue
                if nx == rex and ny == rey:
                    sw = 1
                q.append([nx, ny, bx, by, d+1, sw, 1])
                chk[nx][ny][bx][by] = 1
                visit[1][nx][ny] = 1
        else:
            for i in range(4):
                nx, ny = rx + dirx[i], ry + diry[i]
                sw = 0
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if maze[nx][ny] == 5:
                    continue
                if board[0][nx][ny] <= d and visit[0][nx][ny] == 1:
                    continue
                for j in range(4):
                    nx2, ny2 = bx + dirx[j], by + diry[j]
                    sw2 = 0
                    if nx2<0 or nx2>=n or ny2<0 or ny2>=m:
                        continue
                    # if board[0][nx][ny] != board[1][nx2][ny2]:
                    #     continue
                    if maze[nx2][ny2] == 5:
                        continue
                    if board[1][nx2][ny2] <= d and visit[1][nx2][ny2] == 1:
                        continue
                    if nx == nx2 and ny == ny2:
                        continue
                    if chk[nx][ny][nx2][ny2] == 1:
                        continue
                    if nx == bx and ny == by and nx2 == rx and ny2 == ry: # 서로 위치가 바뀐거
                        continue
                    if nx == rex and ny == rey:
                        sw = 1
                    if nx2 == bex and ny2 == bey:
                        sw2 = 1
                    q.append([nx, ny, nx2, ny2, d+1, sw, sw2])
                    chk[nx][ny][nx2][ny2] = 1
                        
                        
                    
    
    return answer
