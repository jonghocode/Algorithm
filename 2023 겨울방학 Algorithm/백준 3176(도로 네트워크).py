# 깊이, 부모, 최솟값 저장, 최댓값 저장(logN 만큼 올라가므로 계속 부모와 부모의 부모의 최대, 최소만 기록해주면 된다.
import sys
from collections import deque

def bfs(): # 1로 기준 잡기(이 문제에서는 어떤node로 잡아도 상관없음
    q = deque([(1)]); chk = set(); chk.add(1)
    d[1] = 1

    while q:
        now = q.popleft()

        for e, w in graph[now]:
            if e not in chk:
                q.append(e)
                chk.add(e)
                d[e] = d[now] + 1
                p[0][e] = now
                cost[0][e] = w
                cost2[0][e] = w


n = int(input())
t, h = 1, 0
while t <= n:
    t *= 2
    h += 1

graph = {i : [] for i in range(n+1)}
d, p = [0 for _ in range(n+1)], [[0 for _ in range(n+1)] for _ in range(h+1)]
cost = [[0 for _ in range(n+1)] for _ in range(h+1)] # 최솟값 저장 희소배열
cost2 = [[0 for _ in range(n+1)] for _ in range(h+1)] # 최댓값 저장 희소배열
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

bfs()

for i in range(1, h+1):
    for j in range(1, n+1):
        p[i][j] = p[i-1][p[i-1][j]]
        # 나 -> 부모, 부모 -> 부모의 부모 중 작은 값 기록
        cost[i][j] = min(cost[i-1][j], cost[i-1][p[i-1][j]])
        cost2[i][j] = max(cost2[i-1][j], cost2[i-1][p[i-1][j]])

m = int(input())
for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    MIN, MAX = int(1e12), 0

    if d[n1] < d[n2]:
        t = n1; n1 = n2; n2 = t
    
    num = d[n1] - d[n2]
    for j in range(h+1):
        if num & 1 << j:
            # max값, min값을 구해준다. 원래 이 자리에 n1을 바꿔주는 코드가 있었는데
            # 3퍼센트에서 계속 틀려서 바꿔주니 통과했다.
            MIN = min(MIN, cost[j][n1])
            MAX = max(MAX, cost2[j][n1])
            n1 = p[j][n1]

    if n1 == n2:
        print(MIN, MAX)
        continue

    for j in range(h, -1, -1):
        if p[j][n1] != p[j][n2]:
            MIN = min(MIN, min(cost[j][n1], cost[j][n2]))
            MAX = max(MAX, max(cost2[j][n1], cost2[j][n2]))
            n1 = p[j][n1]
            n2 = p[j][n2]
    
    MIN = min(MIN, min(cost[0][n1], cost[0][n2]))
    MAX = max(MAX, max(cost2[0][n1], cost2[0][n2]))
    print(MIN, MAX)