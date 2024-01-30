import sys

def dfs(root, sum):
    global answer
    temp = []
    for e, w in graph[root]:
        k = dfs(e, w)
        temp.append(k)
        visit[root] = max(visit[root], k)
    temp.sort()
    if len(temp) >= 2: # 둘 중 최댓값으로 값 구해주기
        answer = max(answer, temp[-1] + temp[-2])
    elif len(temp) == 1: # 하나로만 뻗어져 가는 경우
        answer = max(answer, temp[0])
    return visit[root] + sum # 이번에 들어온 간선값과 현재 값을 더해서 return 해줌

n = int(input())
graph = {i : [] for i in range(n+1)}
for _ in range(n-1):
    parent, child, w = map(int, sys.stdin.readline().split())
    graph[parent].append((child, w))

answer = 0
visit = [0 for _ in range(n+1)]
dfs(1, 0)
print(answer)