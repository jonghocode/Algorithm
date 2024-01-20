import sys
from heapq import *

n, m = map(int, input().split())
graph = {i : [] for i in range(n+1)}
chk = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    chk[b] += 1

q = []
for i in range(1, n+1):
    if chk[i] == 0:
        heappush(q, i)
        chk[i] -= 1

while q:
    now = heappop(q)
    print(now, end = ' ')
    for node in graph[now]:
        if chk[node] > 0:
            chk[node] -= 1
            if chk[node] == 0:
                chk[node] -= 1
                heappush(q, node)
