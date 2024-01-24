# 처음에 2차원으로 구현했었는데 2차원으로는 같은곳을 다시 방문을 했을 때 처리르 못 해주는 것이었다.
# 그래서 다른사람의 풀이를 참고했는데 나랑 로직은 똑같지만 3차원 dp 배열을 사용해서 같은곳을 다시 방문할 수 있게 만들었다.
# (1, 1)의 위치를 2번 방문한다 했을 때 처음 방문할 때의 깊이는 1이다. 그래서 dp[1][1][1]에 체크를 하고 3번째에 (1, 1)을 방문한다면
# dp[1][1][3]에 체크를 해버리면 또 방문을 할 수 있게 된다. 오랜만에 3차원 문제를 풀어봐서 감을 잃었나보다.

def dfs(x, y, d):
    if d == len(s)-1: # 메모이제이션은 끝까지 가야함
        return 1
    if dp[x][y][d] != -1:
        return dp[x][y][d]
    dp[x][y][d] = 0
    for i in range(4):
        for j in range(1, k+1):
            nx, ny = x + dirx[i]*j, y + diry[i]*j
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] != s[d+1]:
                continue
            dp[x][y][d] += dfs(nx, ny, d+1)
    
    return dp[x][y][d]
            

n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
s = input()
dp = [[[-1 for _ in range(len(s))] for _ in range(m)]for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == s[0]:
            answer += dfs(i, j, 0)

print(answer)