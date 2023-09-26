# 2 * n * m
# 벽을 부수지 않고 이동
# 벽을 부수고 이동
from collections import deque

n, m = map(int, input().split())
lst, q, zx, zy = [], deque([]), [-1, 1, 0, 0], [0, 0, -1, 1]
# 벽을 부수고 이동하는 2차원배열, 부수지않고 이동하는 2차원배열
wall = [[[0]*1010 for _ in range(1010)] for _ in range(2)]

for _ in range(n):
    lst.append(list(map(int, input())))

q.append([0, 0, 0])

sw = 0
while q:
    x, y, z = q.popleft()
    if x == n-1 and y == m-1:
        sw = 1
        break
    for i in range(4):
        nx = x + zx[i]; ny = y + zy[i]

        if nx<0 or nx>=n or ny<0 or ny>=m: continue
        if lst[nx][ny] == 0 and wall[z][nx][ny] == 0:
            wall[z][nx][ny] = wall[z][x][y] + 1
            q.append([nx,ny,z])
        elif lst[nx][ny] == 1 and z == 0 and wall[1][nx][ny] == 0:
            wall[1][nx][ny] = wall[0][x][y] + 1
            q.append([nx,ny,1])

print()
for i in range(n):
    for j in range(m):
        print(wall[0][i][j], end=" ")
    print()

print()
for i in range(n):
    for j in range(m):
        print(wall[1][i][j], end=" ")
    print()

if sw == 0: print(-1)
else : print(max(wall[0][n-1][m-1]+1, wall[1][n-1][m-1]+1))
