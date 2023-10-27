from collections import deque

start, end = map(int, input().split())
q = deque([])
q.append([start, 0])
visit = [0x7fffffff for _ in range(100010)]
answer = 0x7fffffff
while q:
    x, d = q.popleft()
    
    if x == end:
        answer = min(answer, d)
    if x + 1 <= 100000 and visit[x+1] >= d+1:
        q.append([x+1, d+1])
        visit[x+1] = d+1
    if x - 1 >= 0 and visit[x-1] > d+1:
        q.append([x-1, d+1])
        visit[x-1] = d+1
    if x*2 <= 100000 and visit[x*2] > d:
        q.append([x*2, d])
        visit[x*2] = d

print(answer)