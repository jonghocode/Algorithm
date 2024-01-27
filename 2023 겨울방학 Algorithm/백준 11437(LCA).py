import sys

def saveDepth(before, root, d):
    depth[root][0], depth[root][1] = d, before
    for node in graph[root]:
        if depth[node][0] == -1:
            saveDepth(root, node, d+1)

def findRoot(n1, n2, d1, d2):
    if depth[n1][1] == n2:
        print(n2)
        return
    elif depth[n2][1] == n1:
        print(n1)
        return
        
    if d1 > d2:
        findRoot(depth[n1][1], n2, d1-1, d2)
    elif d1 < d2:
        findRoot(n1, depth[n2][1], d1, d2-1)
    else:
        if depth[n1][1] == depth[n2][1]:
            print(depth[n1][1])
            return
        else:
            findRoot(depth[n1][1], depth[n2][1], d1-1, d2-1)

n = int(input())
graph = {i : [] for i in range(n+1)}
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [[-1 for _ in range(2)] for _ in range(n+1)]
saveDepth(0, 1, 0)

m = int(input())
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    findRoot(n1, n2, depth[n1][0], depth[n2][0])