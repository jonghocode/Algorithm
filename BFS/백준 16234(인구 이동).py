# 그래프 새로 만들고
# 그래프 마다 합을 다 더한 후 (x,y)배열에 저장하면서 이동 후 / 값 고치기
# 반복
from collections import deque

n, l, r = map(int ,input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

def bfs(x, y, test, chk):
    zx, zy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([])
    chk[x][y] = 1
    q.append([x, y])
    sum = 0
    modify = deque([])

    while q:
        nx, ny = q.popleft()
        sum += lst[nx][ny]
        modify.append([nx, ny])
        for i in range(4):
            ax = nx + zx[i]
            ay = ny + zy[i]
            if ax < 0 or ax >= n or ay < 0 or ay >= n:
                continue
            if chk[ax][ay] == 1:
                continue
            if l <= abs(lst[ax][ay] - lst[nx][ny]) <= r:
                q.append([ax, ay])
                chk[ax][ay] = 1

    
    t = len(modify)
    if t == 1:
        return 0
    else :
        for i in range(t):
            dx, dy = modify.popleft()
            lst[dx][dy] = sum//t

        return 1


answer = 0 # 답
while True:
    sw = 0 # 인구 이동이 가능한지
    chk = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if chk[i][j] == 0:
                test = []
                if bfs(i, j, test, chk): # 큐에 다 넣고 인구이동까지
                    sw = 1
    
    if sw == 0:
        break

    answer += 1

print(answer)