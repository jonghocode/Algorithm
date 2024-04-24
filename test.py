# 백준 1865(웜홀)

# 벨만포드 : 총 n번을 도는데 n-1번 만큼 돌고 마지막 n번째에도
# 줄어든다면 무한으로 줄어듬

import sys
input = sys.stdin.readline
MAX = int(1e12)

T = int(input())
for _ in range(T):
    n, m, w = map(int, input().split())
    graph = []
    
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((s, e, t))
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))
    
    dis = [MAX for _ in range(n+1)]
    for i in range(n):
        sw = 0
        for j in graph:
            a, b, c = j
            if dis[b] > dis[a] + c:
                dis[b] = dis[a] + c
                sw = 1
    if  sw == 1:
        print("YES")
    else:
        print("NO")