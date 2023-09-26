import heapq

n = int(input())
board = []
chk = [[0]*n for _ in range(n)]
zx, zy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0x7fffffff

for i in range(n):
    board.append(list(map(int, input())))

    
q = []
heapq.heappush(q, [0, 0, 0])
chk[0][0] = 1

while q:
    d, x, y = heapq.heappop(q)
    if x == n-1 and y == n-1:
        print(d)
        break

    for i in range(4):
        nx = x + zx[i]
        ny = y + zy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if chk[nx][ny] == 1:
            continue
        chk[nx][ny] = 1
        if board[nx][ny] == 0:
            heapq.heappush(q, ([d+1, nx, ny]))
        elif board[nx][ny] == 1:
            heapq.heappush(q, ([d, nx, ny]))
