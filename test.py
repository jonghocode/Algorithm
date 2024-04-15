# 백준 1162(도로포장)
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
MAX = int(1e12)

n, m, k = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
cost = [[MAX for _ in range(n+1)] for _ in range(k+1)]
cost[0][1] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
heappush(q, (0, 1, 0))

while q:
    d, now, cnt = heappop(q)

    if cost[cnt][now] < d:
        continue
    
    for e, w in graph[now]:
        if cost[cnt][e] > d + w: # 포장 x
            cost[cnt][e] = d + w
            heappush(q, (d + w, e, cnt))
        if k > cnt and cost[cnt+1][e] > d:
            cost[cnt+1][e] = d
            heappush(q, (d, e, cnt+1))

answer = MAX
for i in range(k+1):
    answer = min(answer, cost[i][n])
print(answer)