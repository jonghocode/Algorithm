import sys
from collections import deque

n = int(input())
chk = [0 for _ in range(n+1)]
graph = {i : [] for i in range(n+1)}
time = [0]
for i in range(1, n+1):
    temp = list(map(int, sys.stdin.readline().split()))
    time.append(temp[0])
    for j in range(1, len(temp)-1):
        chk[i] += 1
        graph[temp[j]].append(i)

dp = time[:]
q = deque()
for i in range(1, n+1):
    if chk[i] == 0:
        q.append(i)
        chk[i] -= 1
print(time)
print(graph)
while q:
    now = q.popleft()

    for node in graph[now]:
        if chk[node] > 0:
            chk[node] -= 1
            if chk[node] == 0:
                q.append(node)
                chk[node] -= 1
            dp[node] = max(dp[node], dp[now] + time[node])
    print(now, dp)
for i in range(1, n+1):
    print(dp[i])