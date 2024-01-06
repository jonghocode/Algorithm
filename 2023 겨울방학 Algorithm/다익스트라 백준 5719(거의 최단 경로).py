import sys
from collections import deque

INF = 0x7fffffff

def di(start):
    visit = [0 for _ in range(n)]; visit[start] = 1
    cost = [INF for _ in range(n)]; cost[start] = 0
    q = deque([(start)])

    while q:
        now = q.popleft()

        for i in range(n):
            if board[now][i] != INF and visit[i] == 0 and cost[i] > cost[now] + board[now][i]:
                cost[i] = cost[now] + board[now][i]

        MIN = INF
        for i in range(n):
            if visit[i] == 0 and MIN > cost[i]:
                MIN = cost[i]
                idx = i

        if MIN != INF:
            q.append(idx)
            visit[idx] = 1
    
    return cost

def remove(end, chk):
    q = deque([(end)])

    while q:
        now = q.popleft()
        for i in range(n):
            if chk[i] + board[i][now] == chk[now]: # 반대에서 돌아가기 때문에 board[now][i]가 아니라 board[i][now]
                q.append(i)
                board[i][now] = INF


while True:
    n, m = map(int, input().split())
    if not n + m:
        break
    
    st, ed = map(int, input().split())
    board = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        board[i][i] = 0


    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        board[a][b] = c;

    chk = di(st)
    remove(ed, chk)
    lst = di(st)
    print(lst[ed] if lst[ed] != INF else -1)