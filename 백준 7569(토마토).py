from collections import deque

m, n, t = map(int, input().split()) # 열, 행, 박스 수
lst, zero, q = [], 0, deque([])
zx, zy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(t):
    temp = []
    for j in range(n):
        temp.append(list(map(int,input().split())))
        for k in range(m):
            if temp[j][k] == 0: zero += 1
            elif temp[j][k] == 1: q.append([i,j,k,0])
    lst.append(temp)

# 초기값 좌표 저장, 0 개수 구해놓기

# 큐 돌릴때마다 0개수 빼고 0개수가 더이상 줄어들지 않는다면 종료 후 답 출력
answer = 0
while q:
    sum = 0 # 한 번 큐에서 돌릴 때 얼마나 오염되는지
    h, x, y, d = q.popleft()
    answer = d

    for i in range(4): # 앞, 뒤, 오른쪽, 왼쪽
        nx = x + zx[i]; ny = y + zy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >=m: continue
        if lst[h][nx][ny] != 0: continue

        lst[h][nx][ny] = d + 1; sum += 1
        q.append([h, nx,ny,d+1])
    
    # 위
    if h+1 < t and lst[h+1][x][y] == 0:
        lst[h+1][x][y] = d + 1; sum  += 1
        q.append([h+1, x, y, d+1])

    # 아래
    if h-1 >= 0 and lst[h-1][x][y] == 0:
        lst[h-1][x][y] = d + 1; sum  += 1
        q.append([h-1, x, y, d+1])
    
    zero -= sum

if zero != 0: print(-1)
else : print(answer)
print(lst)