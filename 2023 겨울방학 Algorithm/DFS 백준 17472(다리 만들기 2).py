# 구역 나누기 / 연결하기(visit 체크 안 된 섬 중 하나 골라서 돌리기 후 확인)
# 1. 구역 나누기
# 2. 4방향 중 0이 하나라도 있으면 다리 만들어보기
# 3. 만들었다면 최소로 만들기(2차원 배열에 체크)
# -> 모든 1에서 돌리기
# 4. 모두 연결되었는지 확인

from collections import deque

def cntdfs(x, y, cnt): # 영역 구하기
    cntchk[x][y] = cnt
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[nx][ny] == 0 or cntchk[nx][ny] != 0:
            continue
        cntdfs(nx, ny, cnt)

def bridgeDfs(x, y, k, d, what): # 다리 연결하기
    global flag

    if cntchk[x][y] != what and cntchk[x][y] != 0:
        flag = cntchk[x][y]
        return d - 1
    nx, ny = x + dirx[k], y + diry[k]
    if nx < 0 or nx >= n or ny < 0 or ny >= m or cntchk[nx][ny] == what:
        return d - 1

    return bridgeDfs(nx, ny, k, d+1, what)


def mst(bridge): # 최소 스패닝 트리
    mstchk = [0 for _ in range(cnt)]
    mstchk[0] = 1; mstchk[1] = 1
    temp = list(bridge[1])
    cost = temp
    q = deque()
    q.append([1, 0])
    while q:
        now, sum = q.popleft()
        MIN = 0x7fffffff

        for i in range(cnt):
            if mstchk[i] == 0 and MIN > cost[i]:
                MIN = cost[i]
                idx = i

        if MIN != 0x7fffffff:
            q.append([idx, sum + MIN])
            mstchk[idx] = 1

            for i in range(cnt):
                if mstchk[i] == 0 and bridge[idx][i] < cost[i]:
                    cost[i] = bridge[idx][i]

    for i in range(cnt):
        if mstchk[i] == 0:
            return -1
    return sum

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]

cntchk = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and cntchk[i][j] == 0:
            cntdfs(i, j, cnt)
            cnt += 1

visit = [0 for _ in range(cnt)]
bridge = [[0x7fffffff for _ in range(cnt)] for _ in range(cnt)]
answer = 0x7fffffff
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            for k in range(4): # 4방향 중 0이 있으면 그쪽으로 다리 놓아보기
                nx, ny = i + dirx[k], j + diry[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if board[nx][ny] == 1:
                    continue
                flag = -1
                d = bridgeDfs(nx, ny, k, 1, cntchk[i][j])
                
                if d >= 2 and flag != -1: # 다리 놓기
                    if bridge[cntchk[i][j]][flag] > d or bridge[flag][cntchk[i][j]] > d: # 다리를 놓았는데 더 짧은 다리가 나오면 바꾸고 mst함수 호출
                        bridge[cntchk[i][j]][flag] = d
                        bridge[flag][cntchk[i][j]] = d
                        ans = mst(bridge)
                        if ans != -1:
                            answer = min(answer, ans)
            
print(answer if answer != 0x7fffffff else -1)