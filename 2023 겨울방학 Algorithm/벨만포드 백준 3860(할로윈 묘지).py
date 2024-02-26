# 3860번 할로윈 묘지

import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if not m + n:
        break
    graph = []
    dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
    chk = [[0 for _ in range(m)] for _ in range(n)]

    cnt = 1
    MAP = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            MAP[i][j] = cnt
            cnt += 1
    
    g = int(input())
    for i in range(g):
        x, y = map(int, input().split())
        chk[x][y] = -1
    
    e = int(input())
    for i in range(e):
        x1, y1, x2, y2, t = map(int, input().split())
        st, ed = MAP[x1][y1], MAP[x2][y2]
        graph.append((st, ed, t))
        chk[x1][y1] = -2
    
    for i in range(n): # 그래프 생성
        for j in range(m):
            if chk[i][j] == -1 or chk[i][j] == -2 or (i == n-1 and j == m-1): # 도착지에서는 다른곳으로 못가게 해야함 ! 이 부분때문에 문제를 못 풀었었음
                continue
            for k in range(4):
                x, y = i + dirx[k], j + diry[k]
                if x < 0 or x >= n or y < 0 or y >= m: # 범위를 벗어나거나
                    continue
                if chk[x][y] == -1: # 묘비라면
                    continue
                st, ed = MAP[i][j], MAP[x][y]
                graph.append((st, ed, 1))
    
    # 벨만포드
    MAX = int(1e12)
    dis = [MAX for _ in range(cnt)]
    dis[1] = 0 # 시작점(0, 0) -> cnt = 1

    for i in range(1, cnt+1):
        sw = 0
        for temp in graph:
            a, b, c = temp
            if dis[a] == MAX:
                continue
            if dis[b] > dis[a] + c:
                dis[b] = dis[a] + c
                if b == cnt: # 도착지라면 종료
                    break
                sw = 1

    if sw == 1:
        print("Never")
    else:
        print("Impossible" if dis[MAP[n-1][m-1]] == MAX else dis[MAP[n-1][m-1]])