from collections import deque
import sys

n, st, ed = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

q = deque([])
visit = [0 for _ in range(n+1)]
q.append([st, 0, -1])

while q:
    now, sum, m = q.popleft()
    if now == ed:
        print(sum - m)
        exit()
    for i in range(len(graph[now])):
        if visit[graph[now][i][0]] == 0:
            visit[graph[now][i][0]] = 1
            q.append([graph[now][i][0], sum + graph[now][i][1], max(m, graph[now][i][1])])
