import sys

MAX = int(1e12)

while True:
    w, h = map(int, input().split())
    if not w + h:
        break
    
    graph = []
    board = [[0 for _ in range(h)] for _ in range(w)]
    chk = [[0 for _ in range(h)] for _ in range(w)]
    dis = [MAX for _ in range(w*h+1)]; dis[1] = 0
    dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]

    cnt = 1
    for i in range(w):
        for j in range(h):
            board[i][j] = cnt
            cnt += 1

    g = int(input())
    for _ in range(g):
        a, b = map(int, sys.stdin.readline().split())
        chk[a][b] = -1

    e = int(input())
    for i in range(e):
        x1, y1, x2, y2, t = map(int, sys.stdin.readline().split())
        # if x1 == x2 and y1 == y2:
        #     continue
        chk[x1][y1] = -2
        graph.append((board[x1][y1], board[x2][y2], t))

    for i in range(w):
        for j in range(h):
            if chk[i][j] == -1:
                continue
            if chk[i][j] == -2:
                dis[board[i][j]] == MAX
                continue
            if chk[i][j] != 0:
                continue
            for k in range(4):
                x, y = i + dirx[k], j + diry[k]
                if x < 0 or x >= w or y < 0 or y >= h:
                    continue
                if chk[x][y] == -1:
                    continue
                graph.append((board[i][j], board[x][y], 1))
                
    
    for _ in range(1, w*h+1):
        sw = 0
        for i in range(len(graph)):
            a, b, c = graph[i][0], graph[i][1], graph[i][2]
            if dis[a] == MAX:
                continue
            if dis[b] > dis[a] + c:
                dis[b] = dis[a] + c
                sw = 1

    if sw == 1:
        print("Never")
    else:
        if dis[board[w-1][h-1]] == MAX:
            print("Impossible")
        else:
            print(dis[board[w-1][h-1]])