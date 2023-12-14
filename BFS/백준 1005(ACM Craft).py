# acm craft
# 위상정렬(순서가 정해져있음)

import sys
from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = [0]+list(map(int, input().split()))
    chk = [0 for _ in range(n+1)]
    graph = {i : [] for i in range(1, n+1)}
    dp = time[:] # dp 배열 초기화

    for _ in range(k):
        st, ed = map(int, sys.stdin.readline().split())
        graph[st].append(ed)
        chk[ed] += 1 # 받는 개수 체크
    
    last = int(input())

    q = deque()

    for i in range(1, n+1):
        if chk[i] == 0: # 정점이 0 인것만 넣기
            q.append(i)
            chk[i] -= 1
    
    while q:
        now = q.popleft()
        if now == last:
            print(dp[now])
            break

        for end in graph[now]:
            if chk[end] > 0:
                chk[end] -= 1
                dp[end] = max(dp[end], dp[now] + time[end]) # 다음 건물이 지어지기 위해서는 전에 있던 건물들이 다 지어져야 지을 수 있기 때문에 최댓값으로 갱신

        for i in range(1, n+1):
            if chk[i] == 0:
                q.append(i)
                chk[i] -= 1