import sys
from collections import deque

def bfs(k):
    visit = [0 for _ in range(n+1)]
    q = deque()
    q.append(k)
    visit[k] = 1
    cnt = 1
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = 1
                cnt += 1
    
    return cnt


n, m = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

answer = []
for i in range(1, n+1):
    if graph[i]:
        answer.append([i, bfs(i)])
answer.sort(key = lambda x : (-x[1], x[1]))
t = answer[0][1]
result = [answer[0][0]]
for i in range(1, len(answer)):
    if t != answer[i][1]:
        break
    result.append(answer[i][0])
for i in range(len(result)):
    print(result[i], end=' ')