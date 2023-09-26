r, c, k = map(int, input().split())
home, chk, zx, zy = [], [[0]*c for _ in range(r)], [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0
for i in range(r):
    home.append(input())

def back(x, y, d):
    if x == 0 and y == c-1 and d == k:
        answer += 1
        return
    for i in range(4):
        nx = x + zx[i]
        ny = y + zy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c or chk[nx][ny] == 1 or home[nx][ny] == 'T':
            continue
        chk[nx][ny] = 1
        back(nx, ny, d+1)
        chk[nx][ny] = 0

chk[r-1][0] = 1
back(r-1, 0, 1)
print(answer)