import sys
from collections import deque

n, m = map(int, input().split())
graph = {i : [] for i in range(1, n+1)}

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
start, end = map(int, input().split())

def bfs(k):
    q = deque([])
    q.append(start)
    chk = [0]*(n+1)
    chk[start] = 1

    while q:
        num = q.popleft()
        if num == end:
            return 1
        for num2, weight in graph[num]:
            if chk[num2] == 0 and weight >= k:
                q.append(num2)
                chk[num2] = 1

    return 0



l, r, answer = 1, 1000000000, 0

while l <= r:
    mid = (l+r)//2
    if bfs(mid):
        answer = mid
        l = mid + 1
    else :
        r = mid - 1

print(graph)
print(answer)