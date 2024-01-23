import sys
from collections import deque

n = int(input())
m = int(input())
graph = {i : [] for i in range(n+1)}
remove_graph = {i : [] for i in range(n+1)}
chk = [0 for _ in range(n+1)]

for i in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append((b, t))
    remove_graph[b].append((a, t))
    chk[b] += 1

st, ed = map(int, input().split())
q = deque()
for i in range(1, n+1):
    if chk[i] == 0:
        q.append(i)

dp = [0 for _ in range(n+1)]
while q:
    now = q.popleft()

    for e, w in graph[now]:
        if chk[e] > 0:
            chk[e] -= 1
            if chk[e] == 0:
                q.append(e)
            dp[e] = max(dp[e], dp[now] + w)

# ed애서 출발해서 st까지
Q = deque([(ed)])
chk = set()
answer = 0
while Q: # 최장경로 역추적 -> 처음에 2차원 리스트로 방문체크를 했는데 4800ms정도의 시간이 걸렸는데 딕셔너리와 chk를 사용하니 시간이 300ms로 줄었고 메모리 소모도 많이 줄었다.
    now = Q.popleft()
    for e, w in remove_graph[now]:
        if dp[now] == dp[e] + w and (now, e) not in chk:
            Q.append(e)
            chk.add((now, e))
            answer += 1

print(dp[ed])
print(answer)