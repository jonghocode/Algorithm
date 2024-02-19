# 몇 번 보석을 주웠냐, 주울거냐 안주울거냐, 지날거냐 안지날거냐
# 최대한 많은 보석을 주워야 함
# 다리마다 보석을 들고갈 수 있는 최대 개수가 있음
import sys
from collections import deque

n, m, k = map(int, input().split())
graph = {i : [] for i in range(n+1)}
gem = [int(input()) for _ in range(k)]
gem.sort()
dict = {} # 마을의 번호가 1~100까지 있기 때문에 이것을 다 비트값으로 표현하려면 너무 크기때문에 k의 크기만큼 좌표를 압축하기 위해서 dict자료구조를 사용한다.

for i in range(k):
    dict[gem[i]] = i+1

visit = [[0 for _ in range(1 << (k+1))] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = deque([(1, 0, 0)])
visit[1][0] = 1
if gem[1] == 1: # 1번에 보석이 있는 경우
    q.append((1, 1, 1))
    visit[1][1] = 1

answer = 0
while q:
    now, chk, cnt = q.popleft()
    if answer < cnt and now == 1: # 정답 체크
        answer = cnt

    for e, w in graph[now]:
        if visit[e][chk] == 0 and cnt <= w:
            q.append((e, chk, cnt))
            visit[e][chk] = 1
        if e in dict and visit[e][chk | (1 << dict[e])] == 0 and cnt <= w:
            q.append((e, chk | (1 << dict[e]), cnt + 1))
            visit[e][chk | (1 << dict[e])] = 1

print(answer)