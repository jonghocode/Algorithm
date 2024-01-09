# 5719 거의 최단 경로
import sys
from heapq import *
from collections import deque
INF = 1e12

def di(st, ed, graph):
    cost = [INF for _ in range(n+1)]; cost[st] = 0
    visit = [0 for _ in range(n+1)]; visit[st] = 1
    q = deque([(st)])

    while q:
        now = q.popleft()

        for i in range(n):
            if visit[i] == 0 and cost[i] > cost[now] + graph[now][i]:
                cost[i] = cost[now] + graph[now][i]
        
        MIN = INF
        for i in range(n):
            if visit[i] == 0 and cost[i] < MIN:
                MIN = cost[i]
                idx = i
        
        if MIN != INF:
            visit[idx] = 1
            q.append((idx))

    return cost

while True:
    n, m = map(int, input().split())
    if not n + m:
        break
    st, ed = map(int, input().split())
    board = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        board[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        board[a][b] = c
    
    temp = di(st, ed, board)
    que = deque([(ed)])
    while que:
        now = que.popleft()

        for i in range(n):
            if temp[now] == board[i][now] + temp[i]:
                board[i][now] = INF
                que.append(i)
    
    lst = di(st, ed, board)
    print(lst[ed] if lst[ed] != INF else -1)