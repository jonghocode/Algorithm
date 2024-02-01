import sys

def dfs(idx):
    for edge, weight in graph[idx]:
        if dp[0][edge] == (0, 0):
            dp[0][edge] = (idx, weight)
            dfs(edge)

n = int(input())
e = [0]
graph = {i : [] for i in range(n+1)}
dp = []

for _ in range(n): e.append(int(sys.stdin.readline()))

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

k, cnt = 0, 1
while cnt < n:
    cnt *= 2
    k += 1

dp = [[(0, 0) for _ in range(n+1)] for _ in range(k)]
dp[0][1] = (1, 0)
dfs(1)

for i in range(1, k): # 희소배열 크기(log n)
    for j in range(n, -1, -1):
        if dp[i-1][j] != (0, 0): # 값이 있다면
            dp[i][j] = (dp[i-1][dp[i-1][j][0]][0], dp[i-1][j][1] + dp[i-1][dp[i-1][j][0]][1])

answer = [i for i in range(n+1)]
for idx in range(n, 1, -1): # n 길이의 방(각각의 방을 검사)
    temp, now = idx, e[idx]
    for d in range(k-1, -1, -1): # 2^d승 만큼 건너뛰기
        if dp[d][temp][1] > now:
            continue
        now -= dp[d][temp][1]
        temp = dp[d][temp][0]
        if temp == 0:
            temp = 1
        answer[idx] = temp

for i in range(1, n+1): print(answer[i])