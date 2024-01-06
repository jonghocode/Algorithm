import sys
from collections import deque

def di(st, ed):
    q = deque([(st)])
    visit = [0 for _ in range(n+1)]
    cost = [INF for _ in range(n+1)]
    visit[st] = 1
    cost[st] = 0

    while q:
        now = q.popleft()

        for e, w in graph[now]:
            if visit[e] == 0 and cost[e] > cost[now] + w:
                cost[e] = cost[now] + w
        MIN = INF
        for i in range(1, n+1):
            if visit[i] == 0 and MIN > cost[i]:
                MIN = cost[i]
                idx = i

        if MIN != INF:
            q.append(idx)
            visit[idx] = 1
    
    return cost[ed]

INF = 0x7fffffff
n, m = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

u, v = map(int, input().split())
one = di(1, u) + di(u, v) + di(v, n)
two = di(1, v) + di(v, u) + di(u, n)
if one >= INF and two >= INF:
    print(-1)
else:
    print(min(one, two))