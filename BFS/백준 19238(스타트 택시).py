from collections import deque

n, m, oil = map(int, input().split())
board = []
destination = []
for i in range(n):
    board.append(list(map(int, input().split())))
taxix, taxiy = map(int, input().split()) 
# 범위를 0부터 시작하기 때문에 바꿔줌
taxix -=1 
taxiy -=1
for i in range(m):
    destination.append(list(map(int, input().split())))
    destination[i][0]-=1
    destination[i][1]-=1
    destination[i][2]-=1
    destination[i][3]-=1
    # 손님이 있는 곳 -100으로 표시
    board[destination[i][0]][destination[i][1]] = -100
zx, zy = [-1, 1, 0, 0], [0, 0, -1, 1]

def find(ax, ay):
    global n, oil
    chk = [[0]*n for _ in range(n)]
    # 큐 초기화
    # 승객 찾아서 정렬 후 return
    # 리스트에서 빼기
    # board에서도 빼기
    # 오일도 체크
    q = deque([])
    q.append([ax, ay, 0]) # 현재 택시 좌표
    chk[ax][ay] = 1
    temp = [] # 같은 거리에 있는 손님이 많을 수도 있기 때문에 정렬해서 뽑기위해 리스트에 저장

    while q:
        x, y, d = q.popleft()
        if oil-d < 0: # 오일이 부족하면 -1
            return [-1, -1]
        if board[x][y] == -100: # 손님을 만났다면 넣기
           temp.append([x, y, d])
        for i in range(4):
            nx, ny = x + zx[i], y + zy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 범위 체크
                continue
            if chk[nx][ny] == 1: # 방문 체크
                continue
            if board[nx][ny] == 1: # 벽 체크
                continue
            if not len(temp):
                q.append([nx, ny, d+1])
                chk[nx][ny] = 1

    # temp 정렬 후 return(최단거리 짧은 순, 행 번호, 열 번호), oil 빼주고, 손님 없애기
    if len(temp):
        temp.sort(key = lambda x : (x[2], x[0], x[1]))
        board[temp[0][0]][temp[0][1]] = 0
        oil -= temp[0][2]
        return temp.pop(0)
    else:
        return [-1,-1]


def go(sx, sy, ex, ey):
    global n, oil
    chk = [[0]*n for _ in range(n)]
    q = deque([])
    q.append([sx, sy, 0])
    chk[sx][sy] = 1

    while q:
        x, y, d = q.popleft()
        if oil-d < 0:
            return [-1,-1]
        if x == ex and y == ey:
            oil -= d
            oil += d*2
            return [ex,ey]
        for i in range(4):
            nx, ny = x + zx[i], y + zy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if chk[nx][ny] == 1:
                continue
            if board[nx][ny] == 1:
                continue
            q.append([nx, ny, d+1])
            chk[nx][ny] = 1

    return [-1, -1]


while True:
    if len(destination) == 0:
        break
    lst = find(taxix, taxiy)
    #print(lst)
    if lst[0] == -1 and lst[1] == -1: # 태울 승객이 없으면 종료
        break
    if oil < 0: # 오일이 부족하면 종료
        break
    for j in range(len(destination)):
        if lst[0] == destination[j][0] and lst[1] == destination[j][1]:
            #print(destination[j])
            t = go(destination[j][0], destination[j][1], destination[j][2], destination[j][3]) # 도착지 좌표로 보내주기
            taxix, taxiy = t[0], t[1]

            #print(t)
            if taxix == -1 and taxiy == -1: # 오일이 바닥났으면 중간에
                print(-1)
                exit()
            destination.pop(j)
            break

if len(destination):
    print(-1)
else:
    print(oil)
