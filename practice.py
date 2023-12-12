# 옮긴 지역에 있는 대나무가 그 전보다 많아야함
# 어떤 곳에 처음 풀어놓냐, 최대한 많은 칸 방문
# 자신보다 작은것만 갈수있도록 하고 최댓값을 저장
def dfs(x, y):

    if visit[x][y] != -1:
        return visit[x][y]

    visit[x][y] = 1
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[x][y] >= board[nx][ny]:
            continue
        visit[x][y] = max(dfs(nx, ny)+1, visit[x][y])

    return visit[x][y]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[-1]*N for _ in range(N)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if visit[i][j] == -1:
            dfs(i, j)

answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, visit[i][j])
print(answer)