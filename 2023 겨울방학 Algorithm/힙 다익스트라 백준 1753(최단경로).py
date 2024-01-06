import sys
from heapq import *

INF = 0x7fffffff
n, m= map(int, input().split())
s = int(input())
graph = {i : [] for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

q = []
heappush(q, (0, s))
cost = [INF for _ in range(n+1)]
cost[s] = 0
while q:
    d, now = heappop(q)
    if d > cost[now]:
        continue

    for e, w in graph[now]:
        if cost[e] > d + w:
            cost[e] = d + w
            heappush(q, (d + w, e))

for i in range(1, n+1):
    print("INF" if cost[i] == INF else cost[i])