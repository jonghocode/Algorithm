import sys
input = sys.stdin.readline

n, m = map(int, input().split())
MAX = int(1e12)
MAP = [[MAX for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    MAP[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            MAP[i][j] = min(MAP[i][j], MAP[i][k] + MAP[k][j])

answer = 0
for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        if MAP[i][j] != MAX:
            sum += 1
        if MAP[j][i] != MAX:
            sum += 1
    if sum == n-1:
        answer += 1

print(answer)