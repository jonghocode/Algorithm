# 이미 기록이 되어 있다면 그것을 쓰면됨 (실패, 성공 기록)
# 0이면 방문, 1이면 실패, 2이면 성공
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global state
    if x < 0 or x >= n or y < 0 or y >= m: # 성공했다면
        state = 2 # 값 바꾸기
        return
    if visit[x][y] == 0: # 이미 방문한 곳을 또 방문하면 실패
        state = 1
        return
    if visit[x][y] != -1: # 상태 바꾸고 return
        state = visit[x][y]
        return

    visit[x][y] = 0 # 방문체크
    if board[x][y] == 'D': # dfs 들어가기
        dfs(x+1, y)
    elif board[x][y] == 'U':
        dfs(x-1, y)
    elif board[x][y] == 'L':
        dfs(x, y-1)
    elif board[x][y] == 'R':
        dfs(x, y+1)

    visit[x][y] = state # return 되어서 오니까 state는 바뀌어있음 성공이든 실패든

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visit = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visit[i][j] == -1: # 방문하지 않았다면 함수 실행
            state = 0
            dfs(i, j)

answer = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 2: # 성공개수만 카운트
            answer += 1

print(answer)