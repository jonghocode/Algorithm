import sys
from collections import defaultdict
from heapq import *

INF = int(1e12)
while True:
    n, m = map(int, input().split())
    if not n + m:
        break
    
    graph = defaultdict(list)
    ans = 0
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        ans += c
    
    visit = [0 for _ in range(n)];
    cost = [INF for _ in range(n)]; cost[0] = 0
    q = []; heappush(q, (0, 0))

    while q:
        d, now = heappop(q)
        
        if visit[now] == 0:
            visit[now] = 1
            for e, w in graph[now]:
                if visit[e] == 0 and cost[e] > w:
                    cost[e] = w
                    heappush(q, (w, e))

    print(ans - sum(cost))