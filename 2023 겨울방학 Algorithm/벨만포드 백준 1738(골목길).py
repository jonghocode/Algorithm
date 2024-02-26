import sys
from collections import deque

def p(idx):
    if rev[idx] == -1:
        print(idx, end=' ')
        return
    p(rev[idx])
    print(idx, end=' ')


n, m = map(int, input().split())
MAX = int(1e12)
dis = [-MAX for _ in range(n+1)]; dis[1] = 0
rev = [-1 for i in range(n+1)]
graph = []
revgraph = {i : [] for i in range(n+1)}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a, b, c))
    revgraph[b].append((a, c))

q = deque([(n)])
chk = [0 for _ in range(n+1)]
chk[n] = 1
sw = 0
while q:
    now = q.popleft()
    
    for e, w in revgraph[now]:
        if chk[e] == 0:
            q.append(e)
            chk[e] = 1
    

for i in range(n):
    sw = 0
    for j in range(m):
        a, b, c = graph[j]
        if dis[a] == -MAX: continue
        if dis[b] < dis[a] + c:
            dis[b] = dis[a] + c
            rev[b] = a
            if chk[b] == 1:
                sw = 1

if sw == 1:
    print(-1)
else:
    p(n)