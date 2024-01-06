# 시간 복잡도 : 1000 (1000 log 5000) = 천만
import sys
from heapq import *
from collections import deque

def di(idx):
    global answer, ans
    q = []
    heappush(q, (0, 1))
    cost = [INF for _ in range(n+1)]
    cost[1] = 0
    while q:
        d, now = heappop(q)
        if cost[now] < d:
            continue
        for e, w in graph[now]:
            if e == idx:
                continue
            if cost[e] > d + w:
                cost[e] = d + w
                heappush(q, (d+w, e))
                
    return cost

        
n, m = map(int, input().split())
INF = 0x7fffffff
graph = {i : [] for i in range(1, n+1)}
remove = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    remove.append([a, b])

answer = -1
dir = di(-1)
if dir[n] == INF:
    print(-1)
else:
    q = deque([(n)])
    while q:
        now = q.popleft()
        for e, w in graph[now]:
            if dir[now] == dir[e] + w:
                q.append(e)
                temp = di(e)
                if temp[n] == INF:
                    print(-1)
                    exit()
                else:
                    answer = max(answer, temp[n] - dir[n])

print(answer)