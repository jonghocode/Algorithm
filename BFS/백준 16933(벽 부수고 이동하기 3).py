import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
MAP = [0] + [[0] + list(input().strip()) for _ in range(n)]
MAX = int(1e12)
chk = [[[[MAX for _ in range(m+1)] for _ in range(n+1)] for _ in range(k+1)] for _ in range(2)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque([(0, 0, 1, 1, 1)]) # 낮, k, n, m, 몇칸
chk[0][0][1][1] = 1

# 같은 자리 머물러 있기(낮, 밤 바뀜)
# 이동하면 낮, 밤 바뀜
# k번까지 이동가능, 벽은 낮에만 부술 수 있음
answer = MAX
while q:
    now, cnt, x, y, d = q.popleft()

    if x == n and y == m:
        answer = min(answer, d)
    
    next = 1 if now == 0 else 0 # 다음 -> 지금이 낮이면 밤, 밤이면 낮

    if chk[next][cnt][x][y] > d+1: # 가만히 있는 경우
            chk[next][cnt][x][y] = d+1
            q.append((next, cnt, x, y, d+1))

    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 1 or nx > n or ny < 1 or ny > m:
            continue
        if MAP[nx][ny] == '0' and chk[next][cnt][nx][ny] > d+1: # 벽이 아니고 이동하는 경우
            chk[next][cnt][nx][ny] = d+1
            q.append((next, cnt, nx, ny, d+1))

        if MAP[nx][ny] == '1':# 벽이라면
            if now == 0 and cnt < k: # 낮이고 벽을 부술 카운트가 있다면
                if chk[next][cnt+1][nx][ny] > d+1:
                     chk[next][cnt+1][nx][ny] = d+1
                     q.append((next, cnt+1, nx, ny, d+1))
            elif now == 1:
                 q.append((next, cnt, x, y, d+1))

print(-1 if answer == MAX else answer)