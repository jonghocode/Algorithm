# '#'은 지나갈 수 x '.'은 가능
# 'S'는 시작, 'E'는 도착
from collections import deque

dirh, dirx, diry = [1, -1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

while True:
    l, r, c = map(int, input().split())
    if l + r + c == 0:
        break
    board = [[[''for _ in range(c)] for _ in range(r)] for _ in range(l)]
    chk = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    pchk = False

    for i in range(l):
        for j in range(r):
            temp = input()
            for k in range(len(temp)):
                board[i][j][k] = temp[k]
                if board[i][j][k] == 'S':
                    stl, str, stc = i, j, k
                elif board[i][j][k] == 'E':
                    edl, edr, edc = i, j ,k
            
        input()
    
    q = deque([])
    q.append([stl, str, stc, 0])
    chk[stl][str][stc] = 1

    while q:
        h, x, y, d = q.popleft()
        if h == edl and x == edr and y == edc:
            print(f'Escaped in {d} minute(s).')
            pchk = True
            break
        
        # 상,하,좌,우,위,아래
        for i in range(6):
            th, tx, ty = dirh[i]+h, dirx[i]+x, diry[i]+y
            if th < 0 or th >= l or tx < 0 or tx >= r or ty < 0 or ty >= c: # 범위체크
                continue
            if chk[th][tx][ty] == 1:
                continue
            if board[th][tx][ty] == '#':
                continue
            q.append([th,tx,ty,d+1])
            chk[th][tx][ty] = 1

    if pchk == False:
        print('Trapped!')