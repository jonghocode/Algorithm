from heapq import *
import sys

def di(st, ed):
    cost = [INF for _ in range(n+1)]; cost[st] = 0

    q = []
    heappush(q, (0, st))
    while q:
        d, now = heappop(q)
        
        if cost[now] < d:
            continue
        for e, w in graph[now]:
            if cost[e] > cost[now] + w:
                cost[e] = cost[now] + w
                heappush(q, (cost[now] + w, e))
        
    return cost[ed]

INF = 1e12
n, e = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

node1, node2 = map(int, input().split())
one = di(1, node1) + di(node1, node2) + di(node2, n)
two = di(1, node2) + di(node2, node1) + di(node1, n)

print(-1 if one >= INF and two >= INF else min(one, two))