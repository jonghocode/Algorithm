import sys

def dfs(x, y, cnt):
    global answer
    if chk[x][y] != 0:
        if chk[x][y] == cnt: # 이 코드 하나로 시간을 확 줄였다. 원래 bfs를 새로 돌려서 구역의 개수를 새로 구했는데 어차피 사이클을 구하는 것이므로 이렇게 사이클이 만들어지면 답을 더해주면 된다.
            answer += 1
        return chk[x][y]
    else:
        if board[x][y] == 'D':
            chk[x][y] = cnt
            # 계속 가다가 값이 있으면 return이 되는데
            # 그 값과 이 좌표는 같은 level이므로 그 값으로 교체
            t = dfs(x+1, y, cnt)
            chk[x][y] = t
           
        elif board[x][y] == 'U':
            chk[x][y] = cnt
            t = dfs(x-1, y, cnt)
            chk[x][y] = t

        elif board[x][y] == 'L':
            chk[x][y] = cnt
            t = dfs(x, y-1, cnt)
            chk[x][y] = t

        elif board[x][y] == 'R':
            chk[x][y] = cnt
            t = dfs(x, y+1, cnt)
            chk[x][y] = t

    return chk[x][y]

n, m = map(int, input().split())
board = [list(sys.stdin.readline().strip())  for _ in range(n)]
chk = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
cnt = 1
for i in range(n):
    for j in range(m):
        if chk[i][j] == 0: # 구역 정하기
            dfs(i, j, cnt)
            cnt += 1

print(answer)