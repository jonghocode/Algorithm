# 2056(작업)
from collections import deque

n = int(input())
graph = {i : [] for i in range(1, n+1)}
chk, time, dp = [0]*(n+1), [0], [0]
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    num = temp[2:]
    time.append(temp[0])
    dp.append(temp[0])
    for j in num:
        graph[j].append(i)
        chk[i] += 1

q = deque()
for i in range(1, n+1):
    if chk[i] == 0:
        q.append([i, dp[i]])
        chk[i] -= 1

while q:
    now, p = q.popleft()

    for go in graph[now]:
        if chk[go] >= 1:
            chk[go] -= 1
            dp[go] = max(dp[go], dp[now] + time[go])
            
    for i in range(1, n+1):
        if chk[i] == 0:
            q.append([i, dp[i]])
            chk[i] -= 1

print(max(dp))