import sys

def find_root(before, now):
    
    chk[now] = 1
    answer[now] = before
    for node in graph[now]:
        if chk[node] == 0:
            find_root(now, node)
            

n = int(input())
graph = {i : [] for i in range(n+1)}
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

chk = [0 for i in range(n+1)]
answer = [0 for i in range(n+1)]
find_root(0, 1)
for i in range(2, n+1):
    print(answer[i])