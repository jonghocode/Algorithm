# 로봇 조종하기
# 왼쪽, 오른쪽, 아래로 이동
# (0,0) -> (n-1, m-1)

# 다른길로 똑같은 길을 지나갈 때 이미 저장되어있었던
# 깊이가 4고 현재 깊이는 8이다 그럼 갈 수 있냐?(갈 수 있게 해야함)

# 그 전 방향이 아래라면 왼쪽 오른쪽 아래 가능
# 그 전 방향이 왼쪽이라면 왼쪽, 아래 가능
# 그 전 방향이 오른쪽이라면 오른쪽, 아래 가능
# 저장되어있는 값보다 크고 그 전 방향이 아래라면 지나가게
# 저장되어있는 값보다 크고 그 전 방향이 왼쪽, 오른쪽이라면 못지나가게
# 1000*1000*1000(n^3)이다 bfs는 경우의수가 너무 많다 시간초과
# dfs + dp는 풀린다.(시간초과 x)
# 추가로 위를 향한 방향으로 가지 못하는것은 dp를 의심해볼수있다.
from heapq import heappush, heappop
import sys
n, m = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[[-1000 for _ in range(m)] for _ in range(n)] for _ in range(3)]
dirx, diry = [1, 0, 0], [0, -1, 1]
q = []
# x, y, dir, cost
heappush(q, [-board[0][0], 0, 0, 0])
answer = -987654321
while q:
    cost, x, y, dir = heappop(q)
    if x == n-1 and y == m-1:
        answer = max(answer, -cost)
        break
    if visit[dir][x][y] > -cost:
        continue
    for i in range(3):
        if dir == 1 and i == 2:
            continue
        elif dir == 2 and i == 1:
            continue
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visit[i][nx][ny] > -cost + board[nx][ny]:
            continue
        
        visit[i][nx][ny] = -cost + board[nx][ny]
        heappush(q, [-(-cost+board[nx][ny]), nx, ny, i])
    
print(answer)