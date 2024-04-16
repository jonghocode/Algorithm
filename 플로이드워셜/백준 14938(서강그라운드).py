# 백준 14938(서강그라운드) - 플로이드 워셜 -> (모든 정점 -> 모든 정점)

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
cost = [0] + list(map(int, input().split()))
MAX = int(1e12)
graph = [[MAX for _ in range(n+1)] for _ in range(n+1)]

for _ in range(r): # 갈 수 있는 길을 최소로 만들기
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[a][b], c)

for k in range(1, n+1): # 경유해서 갈 수 있는지 확인
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        if graph[i][j] <= m: # m 보다 작게 갈 수 있다면 더하기
            sum += cost[j]
    sum += cost[i]
    answer = max(answer, sum)
print(answer)