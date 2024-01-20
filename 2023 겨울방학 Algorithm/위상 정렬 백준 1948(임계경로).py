import sys
from collections import deque

n = int(input())
m = int(input())
graph = {i : [] for i in range(n+1)}
remove_graph = {i : [] for i in range(n+1)}
chk = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    remove_graph[b].append((a, c))
    chk[b] += 1

st, ed = map(int, input().split())
q = deque([(st, 1)])
chk[st] -= 1
while q:
    now, d = q.popleft()

    for e, w in graph[now]:
        if chk[e] > 0:
            chk[e] -= 1
            if chk[e] == 0:
                q.append((e, d+1))
                chk[e] -= 1
        
            dp[e] = max(dp[e], w + dp[now])

q = deque([(ed, 1)])
while q:
    now, d = q.popleft()

    for e, w in remove_graph[now]:
        if dp[now] == dp[e] + w:
            q.append((e, d+1))

print(dp[ed])
print(d+1)