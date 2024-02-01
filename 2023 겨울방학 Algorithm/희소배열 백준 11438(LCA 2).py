import sys

def dfs(before, root, d):

    parent[root][0], parent[root][1] = before, d
    for node in graph[root]:
        if parent[node][0] == -1:
            dfs(root, node, d+1)

n = int(input())
graph = {i : [] for i in range(n+1)}
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [[-1, -1] for _ in range(n+1)]
dfs(0, 1, 0)

m = int(input())
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    