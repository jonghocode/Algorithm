# 바구니 물 양 제한 x
# 1 ~ n
# 1 왼쪽에는 n

# 구름 이동 -> 1 증가 -> 구름 사라짐 -> 물이 증가한 칸에서 대각선으로(경계벗어나지 않은)
# 바구니 수 만큼 물 증가 -> 물의 양이 2이상 모든 칸 구름 생기고 2 줄어듬 새로 생긴 칸은
# 그 전에 사라진 칸 x
import sys

def check(cloud): # 현재 구름이 어떤 좌표인지 return
    global n
    temp = []
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                temp.append([i,j])
    return temp   

n, m = map(int, input().split())
board = []
command = []
cloud = [[0 for _ in range(n)] for _ in range(n)]
cloud[n-1][0] = 1
cloud[n-1][1] = 1
cloud[n-2][0] = 1
cloud[n-2][1] = 1

dirx, diry = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1]
zx, zy = [-1, -1, 1, 1], [-1, 1, 1, -1]

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(m):
    command.append(list(map(int, sys.stdin.readline().strip().split())))

    d, s = command[i][0], command[i][1]

    now = check(cloud) # 현재 구름 좌표
    water = []

    for x, y in now: # 구름 이동
        cloud[x][y] = 0
        # 범위 처리
        # for _ in range(s): # 이 부분도 원래는 %를 이용해서 하려고했었는데 답이 잘 나오지 않아서 이렇게 바꿨다
        #     x, y = x + dirx[d], y + diry[d]
        #     if x < 0:
        #         x = n-1
        #     if y < 0:
        #         y = n-1
        #     if x >= n:
        #         x = 0
        #     if y >= n:
        #         y = 0
        nx, ny = (x + dirx[d]*s)%n, (y + diry[d]*s)%n
        # 7%3 == 1 / -7%3 == 2


        # cloud[tx][ty] = -1 
        # 원래 이 자리에 있었는데 디버깅을 하다보니 -1로 바꿔버리면 위에서 다시 0으로 바뀔수도 있어서 밑에서 바꿔야 함
        # 구현은 시키는대로 잘 하면 된다! 순서에 맞게
        board[nx][ny] += 1
        water.append([nx, ny])
        
    for x, y in water: # 물복사 버그
        cnt = 0
        for k in range(4):
            nx, ny = x + zx[k], y + zy[k]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and board[nx][ny] >= 1:
                cnt += 1
        board[x][y] += cnt
        cloud[x][y] = -1
    
    for r in range(n): # 구름 초기화
        for c in range(n):
            if board[r][c] >= 2 and cloud[r][c] != -1:
                cloud[r][c] = 1
                board[r][c] -= 2
            if cloud[r][c] == -1:
                cloud[r][c] = 0

sum = 0
for i in range(n):
    for j in range(n):
        sum += board[i][j]

print(sum)