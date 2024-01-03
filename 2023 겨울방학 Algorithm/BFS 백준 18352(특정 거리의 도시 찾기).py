import sys
from collections import deque

n, m, k, x = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
visit = [0x7fffffff for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

q = deque()
q.append([x, 0])
visit[x] = 0
answer = 0
while q:
    now, d = q.popleft()
    
    for go in graph[now]:
        if visit[go] > d + 1:
            q.append([go, d+1])
            visit[go] = d + 1

for i in range(1, n+1):
    if visit[i] == k:
        print(i)
        answer = 1

if answer == 0:
    print(-1)