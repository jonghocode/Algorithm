import sys
from collections import deque

n = int(input())
m = int(input())
graph = {i : [] for i in range(n+1)}
chk = [0 for _ in range(n+1)]
answer = [{} for _ in range(n+1)]
for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[y].append((x, k))
    chk[x] += 1

base = set()
q = deque([])
for i in range(1, n+1):
    if chk[i] == 0:
        q.append(i)
        base.add(i)

while q:
    now = q.popleft()

    for e, w in graph[now]:
        if chk[e] > 0:
            chk[e] -= 1
            if now not in base:
                for k, v in answer[now].items():
                    if k not in answer[e]:
                        answer[e][k] = v * w
                    else:
                        answer[e][k] += (v * w)
            else:
                if now not in answer[e]:
                    answer[e][now] = w
                    
            if chk[e] == 0:
                q.append(e)

result = sorted([(k, v) for k, v in answer[n].items()], key = lambda x : x[0])
for k, v in result:
    print(k, v)