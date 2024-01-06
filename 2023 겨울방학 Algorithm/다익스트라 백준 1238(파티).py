from collections import deque
import sys

def di(go):
    q = deque([(x)])
    cost = [INF for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    cost[x] = 0; visit[x] = 1

    while q:
        now = q.popleft()

        for idx, c in go[now]:
            if visit[idx] == 0 and cost[now] + c < cost[idx]:
                cost[idx] = cost[now] + c
        
        MIN = INF
        for i in range(1, n+1):
            if visit[i] == 0 and cost[i] < MIN:
                MIN = cost[i]
                idx = i
        if MIN != INF:
            q.append(idx)
            visit[idx] = 1

    answer.append(cost)

INF = 0x7fffffff
n, m, x = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
graph2 = {i : [] for i in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph2[b].append([a, c])

answer = []
di(graph)
di(graph2)
MAX = -1
for i in range(1, n+1):
    if i == x:
        continue
    MAX = max(MAX, answer[0][i] + answer[1][i])
print(MAX)