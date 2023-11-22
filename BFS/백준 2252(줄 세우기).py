# 위상 정렬 (순서가 정해져있는 작업을 차례로 수행해야 할 때 그 순서를 결정해주기 위한 알고리즘)
# 사이클이 발생하지 않는 방향 그래프
# 여러개의 답이 존재 가능
# 진입 차수가 0인 정점 큐에 삽입 -> 큐에서 꺼내서 연결된 간선 제거
# -> 반복 (큐가 빌 때 까지)
from collections import deque
import sys

n, m = map(int, input().split())
visit, graph = [0 for _ in range(n+1)], {i : [] for i in range(1, n+1)}

for _ in range(m):
    st, ed = map(int, sys.stdin.readline().split())
    visit[ed] += 1
    graph[st].append(ed)

q = deque()
for i in range(1, n+1):
    if visit[i] == 0:
        # 처음 이 부분에 len(graph[i]) != 0 이 부분을 넣었었는데
        # 이 부분을 넣어버리면 키를 비교하지 않은 사람은 큐에 들어가지 않아서
        # 답이 나오지 않는다.
        # 키를 비교하지 않은 사람은 어느 부분에 들어가든 상관없다.
        q.append(i)

while q:
    now = q.popleft()
    print(now, end =' ')
    for i in range(len(graph[now])):
        visit[graph[now][i]] -= 1 # 간선 제거
        if visit[graph[now][i]] == 0: # 진입 차수가 0이면 큐에 넣기
            q.append(graph[now][i])