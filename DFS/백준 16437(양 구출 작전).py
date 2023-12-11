# 방향 비순환 그래프
import sys
from collections import deque

n = int(input())
chk = [0 for _ in range(n+1)] # 자신이 몇 개 받았는지
graph = [[] for _ in range(n+1)]

for i in range(2, n+1):
    t, a, p = map(str, sys.stdin.readline().strip().split())
    a = int(a); p = int(p)
    if t == 'W': # 늑대라면 -로 바꿔주기
        a = -a
    graph[i] = [p, a] # 어디방향, 몇 마리
    chk[p] += 1

graph[1] = [0, 0]

q = deque()
for i in range(2, n+1):
    if chk[i] == 0: # 정점의 카운트가 0이라면 넣어주기
        q.append([i, graph[i][1]])

while q:
    now, sum = q.popleft() # 현재 정점, 몇 마리

    if sum > 0 and graph[graph[now][0]]: # 현재가 수가 양수이고, 다음 정점으로 이동할 수 있으면
        graph[graph[now][0]][1] += sum # 다음 정점의 마리수를 더해줌

    chk[graph[now][0]] -= 1 # 선택을 받은 것이니 체크

    if chk[graph[now][0]] == 0: # 0이라면 넣어주기
        q.append([graph[now][0], graph[graph[now][0]][1]])

print(graph[1][1]) # 1번 정점으로 값이 다 모이게 된다.