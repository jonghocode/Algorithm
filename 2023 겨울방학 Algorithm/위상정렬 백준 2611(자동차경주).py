import sys
from collections import deque

n = int(input())
m = int(input())
graph = {i : [] for i in range(n+1)}
remove_graph = {i : [] for i in range(n+1)}
chk, dp = [0 for _ in range(n+1)], [0 for _ in range(n+1)]

for _ in range(m):
    st, ed, cost = map(int, sys.stdin.readline().split())
    graph[st].append((ed, cost))
    remove_graph[ed].append((st, cost))
    chk[ed] += 1

q = deque([(1)])
while q:
    now = q.popleft()

    for e, w in graph[now]: # 최장 경로 구하기
        if chk[e] > 0:
            chk[e] -= 1
            if chk[e] == 0:
                q.append(e)
            dp[e] = max(dp[e], dp[now] + w)

answer = [1]
Q = deque([(1)])
while Q:
    now = Q.popleft()
    
    for e, w in remove_graph[now]: # 경로 추적
        if dp[now] == dp[e] + w:
            answer.append(e)
            Q.append(e)

answer.append(1)
print(dp[1])
print(*answer[::-1])