# 이 문제를 풀 때 처음에 생각으로만 풀려고 하다가 좀 복잡해져서
# 그래프를 직접 그리니까 확실히 풀기 쉬워졌다.
# 기본 부품은 다음부품에 더해주기만 하고 중간 부품은 다음 부품에 곱해주는 식으로 풀었다.

import sys
from collections import deque

n = int(input())
m = int(input())
graph = {i : [] for i in range(n+1)}
chk = [0 for _ in range(n+1)]
answer = [{} for _ in range(n+1)]
for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    graph[y].append((x, k))
    chk[x] += 1

base = set()
q = deque([])
for i in range(1, n+1):
    if chk[i] == 0:
        q.append(i)
        base.add(i)

while q:
    now = q.popleft()

    for e, w in graph[now]:
        if chk[e] > 0:
            chk[e] -= 1
            if now not in base: # 중간 부품이라면 곱해주기
                for k, v in answer[now].items():
                    if k not in answer[e]:
                        answer[e][k] = v * w
                    else:
                        answer[e][k] += (v * w)
            else: # 기본 부품이라면 다음거에 그냥 추가
                if now not in answer[e]:
                    answer[e][now] = w

            if chk[e] == 0:
                q.append(e)

result = sorted([(k, v) for k, v in answer[n].items()], key = lambda x : x[0])
for k, v in result:
    print(k, v)