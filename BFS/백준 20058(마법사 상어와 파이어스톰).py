import copy
from collections import deque

def bfs(i, j, chk):
    global n

    q = deque()
    chk[i][j] = 1
    q.append([i, j])
    cnt = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dirx[k], y + diry[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if chk[nx][ny] == 1 or board[nx][ny] == 0:
                continue
            q.append([nx, ny])
            chk[nx][ny] = 1
            cnt += 1
    return cnt

n, q = map(int, input().split())
n = 2**n
board = [list(map(int, input().split())) for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
q = list(map(int, input().split()))

for z in range(len(q)):
    L = 2**q[z]
    
    temp = [[0 for _ in range(n)] for _ in range(n)]
    chk = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    if L >= 2:
        while True:
            # x 는 0부터 l까지
            # y가 범위를 벗어난다면 x의 기준을 바꾸기
            tx = x-1
            ty = y+L-1
            for i in range(x, x+L):
                tx = x
                for j in range(y, y+L):
                    temp[tx][ty] = board[i][j]
                    tx+=1
                ty -= 1
            
            y += L
            if y >= n-1:
                x += L
                y = 0
            if x >= n-1:
                break
    else:
        temp = copy.deepcopy(board)
        
    for i in range(n):
        for j in range(n):
            if temp[i][j] >= 1:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dirx[k], j + diry[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if temp[nx][ny] > 0:
                        cnt += 1   
                if cnt < 3:
                    chk[i][j] = 1
    for i in range(n):
        for j in range(n):
            if chk[i][j] == 1:
                temp[i][j] -= 1
    board = copy.deepcopy(temp)
    
    # lst를 다시 board로 넣기
sum = 0
for i in range(n):
    for j in range(n):
        sum += temp[i][j]
print(sum)

t = -1
chk = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if chk[i][j] == 0 and board[i][j] > 0:
            t = max(t, bfs(i, j, chk))
print(t)
            
# r, c에는 얼음의 양
# L은 2^l * 2^l 만큼 나누기
# 모든 격자 부분 회전
# 각 격자 안에서 모든 칸에 대해 4 방향을 확인 후 chk배열에 1이 줄어들것인지 표시

# 1,1 - 1,n
# 1,2 - 2,n
# 1,3 - 3,n
# 1,4 - 4,n

# 2,1 - 1,3
# 2,2 - 2,3
# 2,3 - 3,3
# 2,4 - 4,3

# 1,5 - 1,8
# 1,6 - 2,8
# 1,7 - 3,8
# 



# 원본배열의 y값이 복사배열의 x로 가고, 복사배열의 y는 n-1부터 0까지 줄어들게
# 2중 for문에서 돈다