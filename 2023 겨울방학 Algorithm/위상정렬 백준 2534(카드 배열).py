from heapq import *
import sys

def fun(temp, check, cnt):
    q, visit = [], [i for i in range(k)]
    for i in range(k):
        if check[i] == 0:
            heappush(q, i)
    if cnt == n-k:
        t = 1
    else:
        t = -1
    while q:
        now = heappop(q)
        visit[now] = cnt
        cnt += t
        for node in temp[now]:
            if check[node] > 0:
                check[node] -= 1
                if check[node] == 0:
                    heappush(q, node)
    
    return visit


n, k, p = map(int, input().split())
graph = {i : [] for i in range(n)}
reverse_graph = {i : [] for i in range(n)}
chk, reverse_chk = [0 for _ in range(k)], [0 for _ in range(k)]
div = 1000000007

for _ in range(p):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a); chk[a] += 1
    reverse_graph[a].append(b); reverse_chk[b] += 1



MIN = fun(graph, chk, k-1)
MAX = fun(reverse_graph, reverse_chk, n-k)

answer = 0
r = 1
for i in range(k):
    answer += (MAX[i] - MIN[i]) * r
    r = (r * n) % div

print(answer % div)