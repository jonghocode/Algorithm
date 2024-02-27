# 1738번 골목길(O)
import sys
from collections import deque
input = sys.stdin.readline

def p(idx):
    if rev[idx] == -1:
        return
    p(rev[idx])
    print(idx)


n, m = map(int, input().split())
MAX = int(1e12)
graph = []
rev_graph = {i : [] for i in range(n+1)}
for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
    rev_graph[b].append(a)

q = deque([(n)])
chk = [0 for _ in range(n+1)]; chk[n] = 1
while q:
    now = q.popleft()
    for e in rev_graph[now]:
        if chk[e] == 0:
            q.append(e)
            chk[e] = 1

dis = [-MAX for _ in range(n+1)]; dis[1] = 0
rev = [-1 for _ in range(n+1)]

for i in range(1, n+1):
    sw = 0
    for temp in graph:
        a, b, c = temp
        if dis[a] == -MAX:
            continue
        if dis[b] < dis[a] + c:
            dis[b] = dis[a] + c
            rev[b] = a
            if chk[a] == 1:
                sw = 1

if sw == 0:
    print(p(n))
else:
    print(-1)