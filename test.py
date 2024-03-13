import sys
input = sys.stdin.readline

def dfs(now, k):
    d[now] = k
    for e in graph[now]:
        dfs(e, k+1)


T = int(input())
for _ in range(T):
    n = int(input())
    p = [i for i in range(n+1)]
    d = [0 for i in range(n+1)]
    chk = [0 for _ in range(n+1)]
    graph = {i : [] for i in range(n+1)}
    for _ in range(n-1):
        a, b = map(int, input().split()) # a가 b의 부모
        p[b] = a
        chk[b] = 1
        graph[a].append(b)
    
    for i in range(1, n+1):
        if chk[i] == 0:
            root = i
    

    dfs(root, 1)
    n1, n2 = map(int, input().split())
    
    if d[n1] < d[n2]:
        n1, n2 = n2, n1
    
    for i in range(d[n1] - d[n2]):
        n1 = p[n1]

    if n1 == n2:
        print(n1)
        continue

    for i in range(d[n1]):
        if n1 == n2:
            print(n1)
            break
        n1 = p[n1]
        n2 = p[n2]