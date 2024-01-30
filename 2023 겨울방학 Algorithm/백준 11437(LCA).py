import sys
from collections import deque

def bfs():
    q = deque([(0, 1, 0)])

    while q:
        before, root, d = q.popleft()
        parent[root][0], parent[root][1] = before, d
        for node in graph[root]:
            if parent[node][0] == -1:
                q.append((root, node, d+1))

n = int(input())
graph = {i : [] for i in range(n+1)}
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [[-1, -1] for _ in range(n+1)]
bfs()

m = int(input())
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())

    while True:
        if n1 == n2:
            print(n1)
            break
        if parent[n1][1] < parent[n2][1]:
            n2 = parent[n2][0]
        elif parent[n1][1] > parent[n2][1]:
            n1 = parent[n1][0]
        else:
            n1, n2 = parent[n1][0], parent[n2][0]