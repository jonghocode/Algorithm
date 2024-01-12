from collections import defaultdict
from heapq import *
import sys

INF = int(1e12)
n = int(input())
for _ in range(n):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s))
    
    cost = [INF for _ in range(n+1)]; cost[c] = 0
    q = []; heappush(q, (0, c))
    
    while q:
        d, now = heappop(q)

        if cost[now] < d:
            continue
        for e, w in graph[now]:
            if cost[e] > cost[now] + w:
                cost[e] = cost[now] + w
                heappush(q, (cost[now] + w, e))

    answer, MAX = 0, -1
    for i in cost:
        if i != INF:
            answer += 1
            MAX = max(MAX, i)
    print(answer, MAX)