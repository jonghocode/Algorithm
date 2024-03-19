# 1967 트리의 지름
# 끝까지 갔다가 왼쪽, 오른쪽 중 큰놈을 올린다.
# 왼쪽 오른쪽을 더한 값을 정답으로 계속 최신화 한다.
import sys
input = sys.stdin.readline

def dfs(now, sum):
    global answer
    temp = []
    for e, w in graph[now]:
        k = dfs(e, w)
        temp.append(k)
        visit[now] = max(visit[now], k)

    temp.sort()
    if len(temp) >= 2:
        answer = max(answer, temp[-1] + temp[-2])
    elif len(temp) == 1:
        answer = max(answer, temp[-1])
    return visit[now] + sum

n = int(input())
answer = 0
graph = {i : [] for i in range(1, n+1)}
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

visit = [0 for _ in range(n+1)]
dfs(1, 0)
print(answer)