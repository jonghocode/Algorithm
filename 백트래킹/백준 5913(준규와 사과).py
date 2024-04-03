# (1, 1)과 (5, 5)에서 시작 / (1, 1), (5, 5)에는 무조건 사과 있음
# 인접한 칸으로 이동(사과가 있는 칸, 수확 마친 칸 x)
# 마지막에 같은 칸에서 만나기(마지막을 제외하고는 만날 수 없음)
# 사과를 수확하는 방법의 수
# 1. 아무 좌표 하나에서 출발해서 (1, 1), (5, 5) 두개에 도착한 후 끝까지 갔을 때 돌아오면서 경우의 수 세기(다 chk되어있는지도 봐야함)
# ! 처음에는 위 방법처럼 생각했었다. 메모이제이션을 이용하면서 갔다가 오려고 하니까 좌표를 두개 써야하다보니 너무 복잡해지고 답도 안나왔다.
# 그래서 다른 사람들의 풀이를 보니까 처음 (1, 1) 좌표에서 출발한 다음 (5, 5)에 도착하는 것만 카운트해주면 되는것이었다.
# 저 풀이를 보고 다시 생각해보니 이렇게 문제를 간단히 풀 수 있는 능력을 길러야한다고 생각했다. 더 깊이 고민해야한다.

def dfs(x, y, d):
    global answer

    if x == 5 and y == 5 and d == total:
        answer += 1
        return
    
    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if nx < 1 or nx > 5 or ny < 1 or ny > 5 or chk[nx][ny] == 1 or board[nx][ny] == 1:
            continue
        chk[nx][ny] = 1
        dfs(nx, ny, d+1)
        chk[nx][ny] = 0


n = int(input())
board = [[0 for _ in range(6)] for _ in range(6)]
dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
chk = [[0 for _ in range(6)] for _ in range(6)]
total = 25 - n
answer = 0

for _ in range(n):
    x, y = map(int, input().split())
    board[x][y] = 1

chk[1][1] = 1
dfs(1, 1, 1)
print(answer)