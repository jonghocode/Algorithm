# 각 노드의 깊이와 부모 저장
# 1. 두 노드의 깊이 차이를 구하고 1을 shift하고 차이만큼 and연산을 해서 깊이를 올려준다.
# 2. 깊이를 동일하게 맞춘다. -> 희소배열을 이용해서
# 3. 부모가 다르다면 올린다.

import sys
from collections import deque

def bfs():
    q = deque([(1)]); chk = set(); chk.add(1)
    d[1] = 1
    while q:
        now = q.popleft()
        for e in graph[now]:
            if e not in chk:
                parent[0][e] = now
                chk.add(e)
                q.append(e)
                d[e] = d[now] + 1


n = int(input())
graph = {i : [] for i in range(n+1)}
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

t = 1; h = 0
while t <= n:
    t *= 2
    h += 1 

parent = [[0 for _ in range(n+1)] for _ in range(20)]
d = [0 for _ in range(n+1)]

bfs()

for i in range(1, h+1):
    for j in range(1, n+1):
        parent[i][j] = parent[i-1][parent[i-1][j]]

# for i in range(h):
#     print(parent[i])

m = int(input())
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    # print(n1, n2, parent[0][n1], parent[0][n2])
    
    if d[n1] < d[n2]:
        t = n1; n1 = n2; n2 = t
    num = d[n1] - d[n2]
    for i in range(h+1): # 깊이의 차이만큼 올려준다.
        if num & (1 << i):
            n1 = parent[i][n1]

    if n1 == n2: # 올렸는데 같다면 출력
        print(n1); continue

    for i in range(h, -1, -1): # 부모가 다를때만 올려준다.
        if parent[i][n1] != parent[i][n2]:
            n1 = parent[i][n1]
            n2 = parent[i][n2]

    print(parent[0][n1]) # 부모가 다를때만 올려주었으므로 마지막에 부모를 출력하면 최소공통조상이다.