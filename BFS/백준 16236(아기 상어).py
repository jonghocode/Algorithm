from collections import deque
def eat(x, y):
    global SIZE
    q = deque([])
    q.append([x,y,0]) # 큐 초기화
    
    while q:
        nx, ny, d = q.popleft()
        if lst[nx][ny] < SIZE and lst[nx][ny]!=0: # 먹을 수 있으면 저장
            ans.append([nx, ny, d])
        for k in range(4):
            i = nx + zx[k]; j = ny + zy[k]
            if i<0 or i>=n or j<0 or j>=n: continue
            if chk[i][j] or lst[i][j] > SIZE: 
                continue # 방문했거나 상어크기보다 작으면
            q.append([i,j,d+1])
            chk[i][j] = 1
    if len(ans): return 1
    else : return 0

n = int(input())
lst, SIZE, answer, zx, zy = [], 2, 0, [-1,1,0,0], [0,0,-1,1]

for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if lst[i][j] == 9:
            nowx, nowy = i, j
            lst[i][j] = 0
t = 2
while True:
    ans = []
    chk = [[0]*n for _ in range(n)]
    if eat(nowx, nowy):
        # 깊이가 작은거부터, 위에서부터, 왼쪽에서부터
        ans.sort(key = lambda x : (x[2], x[0], x[1]))

        tx, ty, td = ans[0][0], ans[0][1], ans[0][2]
        lst[tx][ty] = 0
        answer += td
        t -=1
        nowx, nowy = tx, ty

        if t == 0:
            SIZE +=1
            t = SIZE

    else : break # 먹을 물고기가 없으면 종료

print(answer)