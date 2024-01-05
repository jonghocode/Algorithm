import sys
from heapq import heappush, heappop

INF = 0x7fffffff
n, m = map(int, input().split())
board = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    board[a-1].append([c, b-1])
    board[b-1].append([c, a-1])

visit = [0 for _ in range(n)]
cost = [INF for _ in range(n)]
cost[0] = 0
q = []
heappush(q, (0, 0))

while q:
    t, now = heappop(q)
    if visit[now] == 0:
        visit[now] = 1
        for w, idx in board[now]:
            if visit[idx] == 0 and cost[idx] > w:
                cost[idx] = w
                heappush(q, (w, idx))

    
print(sum(cost) - max(cost))