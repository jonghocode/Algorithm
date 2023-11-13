import sys
from collections import deque

n, m, x, y = map(int, input().split())
com = list(map(int, input().split()))

graph = {i : [] for i in range(n)}
q = deque([])
visit = [-1]*n

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

lst = list(map(int, input().split()))

for i in lst:
    q.append([i-1, 0])
    visit[i-1] = 0 # 깊이

while q:
    now, d = q.popleft()
    for i in range(len(graph[now])):
        if visit[graph[now][i]] == -1: # 방문하지 않았다면
            visit[graph[now][i]] = (d+1)*com[graph[now][i]] # 금액 넣기
            q.append([graph[now][i], d+1])


for i in range(n):
    if visit[i] == -1 and com[i] == 0: # 방문하지 않았고 금액이 0원이면 방문체크
        visit[i] = 0

visit.sort(reverse=True)

answer = 0
for i in range(n):
    if i < x:
        answer += visit[i]
    else:
        break

if visit[-1] == -1: # 방문하지 못했다면 -1
    answer = -1

print(answer)
