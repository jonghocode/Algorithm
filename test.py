# 백준 20303(할로윈의 양아치)
import sys
from collections import defaultdict
from collections import deque

def bfs(idx):
    q = deque([(idx)])
    visit[idx] = 1
    d = 1; sum = lst[idx]
    while q:
        now = q.popleft()
        for edge in graph[now]:
            if visit[edge] == 0:
                visit[edge] = 1
                sum += lst[edge]
                d += 1
                q.append(edge)
    return [d, sum]

n, m, k = map(int, input().split())
lst = [0] + list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
answer = []
visit = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if visit[i] == 0:
        answer.append(bfs(i))
        # print(i, answer)

answer.sort(key = lambda x : (-x[1], x[0]))
result = 0
candy = 0
for person, cost in answer:
    if result + person < k:
        result += person
        candy += cost

print(candy)