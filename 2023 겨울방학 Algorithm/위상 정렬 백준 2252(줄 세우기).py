# 방향성
# 작업 순서(작업 순서 못정하면 사이클이 있음)
# 사이클
# 최장경로
from collections import deque
import sys

n, m = map(int, input().split())
graph = {i : [] for i in range(n+1)}
chk = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    chk[b] += 1

q = deque()
for i in range(1, n+1):
    if chk[i] == 0:
        chk[i] -= 1
        q.append(i)

while q:
    now = q.popleft()
    print(now, end =' ')
    for node in graph[now]:
        if chk[node] != 0:
            chk[node] -= 1
            if chk[node] == 0:
                chk[node] -= 1
                q.append(node)