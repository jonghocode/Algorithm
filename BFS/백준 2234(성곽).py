# 각 좌표당 갈 수 있는 곳을 기록
# 방의 개수와, 가장 넓은 방의 넓이는 2중 for문과 bfs
# 각 방 당 현재 자신의 방의 넓이를 기록 해두기 -> 자기 양 사방 중에 한 곳이
# 다른 방이라면 그거 두개 더해보면서 가장 큰 값 구하기
from collections import deque

def remove(i, j, num, room_cnt, wall):
    global n, m

    zx, zy = [-1, 1, 0, 0], [0, 0, -1, 1]
    wall[i][j] = 1
    q = deque([])
    q.append([i, j])
    MAX = -1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + zx[k], y + zy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if wall[nx][ny] != 0:
                continue
            if chk[nx][ny] == num:
                q.append([nx, ny])
                wall[nx][ny] = 1
            elif chk[nx][ny] != num:
                MAX = max(MAX, room_cnt[num] + room_cnt[chk[nx][ny]])

    return MAX

def bfs(chk, num, i, j):
    global n, m
    dirx, diry = [0, -1, 0, 1], [-1, 0, 1, 0]
    chk[i][j] = num
    q = deque([])
    q.append([i, j])
    cnt = 1

    while q:
        x, y = q.popleft()
        possible = where[x][y]
        
        for k in range(4):
            if possible[k] == '1': # 벽이라면
                continue
            nx, ny = x + dirx[k], y + diry[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if chk[nx][ny] != 0:
                continue
            chk[nx][ny] = num
            q.append([nx, ny])
            cnt += 1

    return cnt
    
    



m, n = map(int, input().split())
castle = []
where = []
for i in range(n):
    castle.append(list(map(int, input().split())))
    temp = []
    for j in range(m):
        s = bin(castle[i][j]) # 2진수로 바꾸기
        s = s[2:]
        k = s[::-1]
        while len(k) < 4: # 4자리 맞추기
            k += '0'
        temp.append(k)
    where.append(temp) # (서, 북, 동, 남)

# 1번과 2번은 한 번의 bfs로 구할 수 있음
chk = [[0 for _ in range(m)] for _ in range(n)]
room_cnt = [0]
num = 1 # 방 번호
for i in range(n):
    for j in range(m):
        if chk[i][j] == 0:
            room_cnt.append(bfs(chk, num, i, j))
            num += 1


print(num-1)
print(max(room_cnt))


# 3번 구하기(자신의 옆에 있는 공간이 자신과 다른 공간이라면 그 두개의 방 크기를 더한 것 중에서
# 제일 큰것을 구하기 -> 다른사람들은 m*n*4로 3중 for문을 썼지만 나는 bfs로 구현 이게 더 효율적인듯)
wall = [[0 for _ in range(m)] for _ in range(n)]
answer = -99
for i in range(n):
    for j in range(m):
        if wall[i][j] == 0:
            answer = max(answer,remove(i, j, chk[i][j], room_cnt, wall))
# print(room_cnt)
print(answer)