from collections import deque
import sys

n = int(input())
x, y = map(int, input().split())
t = int(input())

graph = {i:[] for i in range(1,n+1)}

for i in range(t):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

chk = [0]*(n+1)
q = deque([])
q.append([x, 0])
chk[x] = 1

while q:
    k, d = q.popleft()
    if k == y:
        print(d)
        sys.exit(0)
    for i in graph[k]:
        if chk[i] == 0:
            q.append([i, d+1])
            chk[i] = 1

print(-1)