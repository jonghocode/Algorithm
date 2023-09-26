# 입력받기
# 바이러스만 따로 리스트에 모으기
# m개의 조합 구하기
# 퍼트리기

from collections import deque

n, m = map(int, input().split())
board, v, answer, zx, zy = [], [], [], [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 987654321
cnt = 0
for i in range(n):
    board.append(list(map(int, input().split())))

def bfs(answer):
    global cnt
    t = cnt
    chk = [[0]*n for _ in range(n)]
    q = deque([])
    for i,j in answer:
        chk[i][j] = 1
        q.append([i, j, 0])

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                chk[i][j] = 1

    while q:
        x, y, d = q.popleft()
        if board[x][y] == 0:
            t-=1
        if t == 0:
            return d
        
        for i in range(4):
            nx, ny = x + zx[i], y + zy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if chk[nx][ny] == 1: continue
            if board[nx][ny] == 1: continue
            q.append([nx, ny, d+1])
            chk[nx][ny] = 1
            
    return ans
    


def dfs(idx, d): # m개의 조합 구하기
    global ans
    if d == m:
        ans = min(ans,bfs(answer)) # bfs 돌리기
        return
    
    for i in range(idx, len(v)):
        answer.append([v[i][0], v[i][1]])
        dfs(i+1, d+1)
        answer.pop(-1)


for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            v.append([i,j]) # 바이러스만 따로 모으기
        elif board[i][j] == 0:
            cnt+=1

dfs(0, 0)

if ans == 987654321:
    ans = -1
print(ans)
