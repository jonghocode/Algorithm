import sys
sys.setrecursionlimit(10**6)
def dfs(v):
    res = 0
    for i in graph[v]:
        res += dfs(i)
    if lst[v][0] == 'S':
        res += lst[v][1]
    else:
        res -= lst[v][1]
        if res < 0:
            res = 0
    return res
    
n = int(input())
graph = {i : [] for i in range(1, n+1)}
lst = [[0, 0], [0, 0]]

answer = 0
for i in range(n-1):
    what, cnt, num = map(str, sys.stdin.readline().strip().split())
    cnt = int(cnt); num = int(num)
    lst.append([what, cnt])
    graph[num].append(i+2)

print(dfs(1))