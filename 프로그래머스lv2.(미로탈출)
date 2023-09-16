from collections import deque

def solution(maps):
    global answer
    answer = 987654321
    n, m = len(maps), len(maps[0])
    chk = [[0]*m for _ in range(n)]
    zx, zy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'E':
                ex, ey = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j
    
    def Ebfs(x, y):
        q = deque([])
        q.append([x, y, 0])
        chk2 = [[0]*m for _ in range(n)]
        chk2[x][y] = 1
        
        while q:
            nx, ny, d = q.popleft()
            # print(nx, ny, d, "9")
            # for i in range(n):
            #     for j in range(m):
            #         print(chk2[i][j], end=' ')
            #     print()
            # print()
            if nx == ex and ny == ey:
                return d
            for i in range(4):
                ax, ay = nx + zx[i], ny + zy[i]
                if ax < 0 or ax >= n or ay < 0 or ay >= m: continue
                if chk2[ax][ay] != 0: continue
                if maps[ax][ay] == 'X': continue
                chk2[ax][ay] = 1
                q.append([ax, ay, d+1])
        return 987654321
    
    def Lbfs():
        global answer
        
        q = deque([])
        q.append([sx, sy, 0])
        chk[sx][sy] = 1
        
        while q:
            x, y, d = q.popleft()
            print(x, y, d)
            if x == lx and y == ly:
                t = Ebfs(x, y)
                print(t, "111111")
                answer = min(answer, t+d)
            for i in range(4):
                nx, ny = x + zx[i], y + zy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                if chk[nx][ny] != 0: continue
                if maps[nx][ny] == 'X': continue
                q.append([nx, ny, d+1])
                chk[nx][ny] = 1
                
    Lbfs()
    if answer >= 987654321:
        answer = -1
        
    return answer
