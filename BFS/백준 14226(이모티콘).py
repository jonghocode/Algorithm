# 화면, 클립보드, 시간

from collections import deque

s = int(input())
q = deque()
q.append([1, 0, 0])
chk = [[0]*3001 for _ in range(3001)]
chk[1][0] = 1

while q:
    now, store, time = q.popleft()
    # print(now, store, time)
    if now == s:
        break
    if now*2 <= 3000 and chk[now][now] == 0:
        q.append([now, now, time+1])
        chk[now][now] = 1
    if now-1 >= 0 and chk[now-1][store] == 0:
        q.append([now-1, store, time+1])
        chk[now-1][store] = 1
    if store != 0 and now + store <= 3000 and chk[now+store][store] == 0:
        q.append([now+store, store, time+1])
        chk[now+store][store] = 1

print(time)