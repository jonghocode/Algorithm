from collections import deque
import sys

def back(idx):
    if idx == -1:
        return
    back(via[idx])
    answer.append(idx+1)
    

n, m = int(input()), int(input())
INF = 0x7fffffff
board = [[INF for _ in range(n)] for _ in range(n)]
via = [-1 for _ in range(n)]
chk = [0 for _ in range(n)]
for i in range(n):
    board[i][i] = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if board[a-1][b-1] > c:
        board[a-1][b-1] = c

st, ed = map(int, input().split())
st -=1; ed -= 1
q = deque()
q.append(st)
chk[st] = 1
cost = [INF for _ in range(n)]
cost[st] = 0
while q:
    now = q.popleft()

    for i in range(n):
        if board[now][i] + cost[now] < cost[i] and chk[i] == 0:
            cost[i] = board[now][i] + cost[now]
            via[i] = now

    MIN = INF
    for i in range(n):
        if chk[i] == 0 and MIN > cost[i]:
            MIN = cost[i]
            idx = i

    if MIN != INF:
        q.append(idx)
        chk[idx] = 1

answer = []
print(cost[ed])
back(via[ed])
answer.append(ed+1)
print(len(answer))
print(*answer)
