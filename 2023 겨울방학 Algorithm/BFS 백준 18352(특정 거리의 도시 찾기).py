import sys
from collections import deque

n, m, k, x = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
visit = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

