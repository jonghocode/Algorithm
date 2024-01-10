import sys
from heapq import *
from collections import defaultdict

INF = 1e12
n, m, k = map(int, input().split())
graph = defaultdict(list)
answer = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

heappush(answer[1], 0)
q = []
heappush(q, (0, 1))
while q:
    d, now = heappop(q)

    for e, w in graph[now]:
        if len(answer[e]) < k:
            heappush(answer[e], -(d+w))
            heappush(q, (d + w, e))
        elif len(answer[e]) >= k and -answer[e][0] > d + w:
            heappop(answer[e])
            heappush(answer[e], -(d+w))
            heappush(q, (d + w, e))
        
for i in range(1, n+1):
    print(-answer[i][0] if len(answer[i]) == k else -1)
