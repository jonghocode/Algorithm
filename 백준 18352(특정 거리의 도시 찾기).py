from collections import deque
import sys
n, m, k, x = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)

q = deque([])
q.append([x, 0])
chk = [0]*(n+1)
answer = []
chk[x] = 1

while q:
    now, d = q.popleft()
    
    if d == k:
        answer.append(now)
    for i in graph[now]:
        if chk[i] == 0:
            chk[i] = 1
            q.append([i, d+1])

if len(answer):
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)
