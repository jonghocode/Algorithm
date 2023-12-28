n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in  range(n)]
visit = [[0 for _ in range(m+1)] for _ in range(n+1)]
answer = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            visit[i+1][j+1] = min(visit[i][j], visit[i][j+1], visit[i+1][j])+1
            answer = max(visit[i+1][j+1], answer)

print(answer)