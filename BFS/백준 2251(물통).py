from collections import deque
a, b, c = map(int, input().split())
q = deque([])
q.append([0,0,c])
chk = [[[0]*201 for _ in range(201)]for _ in range(201)]
# 한 물통이 비거나, 한 물통이 가득 찰 때 까지
# a가 비어 있을 때 c에 담겨 있을 수 있는 물의 양
chk[0][0][c] = 1
answer = []
while q:
    x, y, z = q.popleft()
    # x -> y
    if x == 0:
        answer.append(z)

    if y + x <= b:
        if chk[0][y+x][z] == 0:
            q.append([0, y+x, z])
            chk[0][y+x][z] = 1
    else:
        if chk[x-(b-y)][b][z] == 0:
            q.append([x-(b-y), b, z])
            chk[x-(b-y)][b][z] = 1
    
    # x -> z
    if z + x <= c:
        if chk[0][y][z+x] == 0:
            q.append([0, y, z+x])
            chk[0][y][z+x] = 1
    else:
        if chk[x-(c-z)][y][c] == 0:
            q.append([x-(c-z), y, c])
            chk[x-(c-z)][y][c] = 1
    
    # y -> x
    if y + x <= a:
        if chk[y+x][0][z] == 0:
            q.append([y+x, 0, z])
            chk[y+x][0][z] = 1
    else:
        if chk[a][y-(a-x)][z] == 0:
            q.append([a, y-(a-x), z])
            chk[a][y-(a-x)][z] = 1
    # y -> z
    if y + z <= c:
        if chk[x][0][z+y] == 0:
            q.append([x, 0, z+y])
            chk[x][0][z+y] = 1
    else:
        if chk[x, y-(c-z), c] == 0:
            q.append([x, y-(c-z), c])
            chk[x][y-(c-z)][c] = 1
    # z -> x
    if z + x <= a:
        if chk[z+x][y][0] == 0:
            q.append([z+x, y, 0])
            chk[z+x][y][0] = 1
    else:
        if chk[a][y][z-(a-x)] == 0:
            q.append([a, y, z-(a-x)])
            chk[a][y][z-(a-x)] = 1
    # z -> y
    if y + z <= b:
        if chk[x][y+z][0] == 0:
            q.append([x, y+z, 0])
            chk[x][y+z][0] = 1
    else:
        if chk[x][b][z-(b-y)] == 0:
            q.append([x, b, z-(b-y)])
            chk[x][b][z-(b-y)] = 1

answer.sort()
print(*answer)
