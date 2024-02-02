# 시작 1, 양방향, 사이클 x, 모든 도시를 방문하는데 걸리는 최소 시간
# 한 도시에서 바로 길이 이어져있는 곳으로 가는 시간은 1
import sys
from collections import deque

def bfs():
    q = deque([(1)]); chk = set(); chk.add(1)
    p[0][1] = 1; d[1] = 1
    while q:
        now = q.popleft()

        for e in graph[now]:
            if e not in chk:
                p[0][e] = now
                d[e] = d[now] + 1
                chk.add(e)
                q.append(e)

n = int(input())
graph = {i : [] for i in range(n+1)}
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

p = [[0 for _ in range(n+1)] for _ in range(20)]
d = [0 for _ in range(n+1)]
bfs()

t = 1; h = 0
while t <= n:
    t *= 2
    h += 1

for i in range(1, h+1):
    for j in range(1, n+1):
        p[i][j] = p[i-1][p[i-1][j]]

m = int(input())
visit = [int(sys.stdin.readline()) for _ in range(m)]
answer = 0
for i in range(1, m):
    n1, n2 = visit[i-1], visit[i]
    if d[n1] < d[n2]:
        t = n1; n1 = n2; n2 = t
    num = d[n1] - d[n2]
    for j in range(h+1):
        if num & (1 << j): # 비트 연산자로 건너 뛸 수 있을 때 바로 건너뛰기
            n1 = p[j][n1]
            answer += (2**j)
    if n1 == n2:
        continue
    
    for j in range(h, -1, -1):
        if p[j][n1] != p[j][n2]:
            n1 = p[j][n1]
            n2 = p[j][n2]
            answer += (2**(j+1)) # 2개가 같이 올라가기 때문에 2배를 더 더해줘야 함 -> j+1

    answer += 2
print(answer)