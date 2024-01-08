import sys
from heapq import *

INF = 1e12
n, m, k = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

q = []
heappush(q, (0, 1, 0))
cost = [[INF for _ in range(n+1)] for _ in range(21)]; cost[0][1] = 0

while q:
    d, now, cnt = heappop(q)

    if cost[cnt][now] < d:
        continue
    for e, w in graph[now]:
        if cost[cnt][e] > d + w:
            cost[cnt][e] = d + w
            heappush(q, (d + w, e, cnt))
        if cnt + 1 <= k and cost[cnt+1][e] > d:
            cost[cnt+1][e] = d
            heappush(q, (d, e, cnt+1))

answer = INF
for i in range(1, k+1):
    answer = min(answer, cost[i][n])
print(answer)