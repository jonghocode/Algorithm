import sys
sys.setrecursionlimit(10**6)
def dfs(root, sum):
    if answer[0] < sum:
        answer[0], answer[1] = sum, root
    chk[root] = 1
    for e, w in graph[root]:
        if chk[e] == 0:
            dfs(e, sum + w)


n = int(input())
graph = {i : [] for i in range(n+1)}
answer = [0, 0]
for i in range(1, n+1):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(temp)-1, 2):
        graph[i].append((temp[j], temp[j+1]))
chk = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if graph[i]:
        dfs(i, 0)
        break
chk = [0 for _ in range(n+1)]
k = answer[1]
answer = [0, 0]
dfs(k, 0)
print(answer)