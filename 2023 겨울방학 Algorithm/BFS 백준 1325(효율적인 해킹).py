import sys
from collections import deque

def dfs(idx):
    if len(graph[idx]) == 0:
        return 1
    if dp[idx] != -1:
        return dp[idx]
    dp[idx] = 1

    for go in graph[idx]:
        dp[idx] += dfs(go)

    return dp[idx]

n, m = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

dp = [-1]*(n+1)
for i in range(1, n+1):
    if graph[i] and dp[i] == -1:
        dfs(i)

k = max(dp)
for i in range(1, n+1):
    if dp[i] == k:
        print(i, end=' ')