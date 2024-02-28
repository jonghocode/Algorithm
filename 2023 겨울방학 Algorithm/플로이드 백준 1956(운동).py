# 1956번 운동(O)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
MAX = int(1e12)
MAP = [[MAX for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            MAP[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    MAP[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            MAP[i][j] = min(MAP[i][j], MAP[i][k] + MAP[k][j])

answer = MAX
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        answer = min(answer, MAP[i][j] + MAP[j][i]) # i에서 j로 갔다가 j에서 i로 오는 최소값이니 사이클도 되고 최솟값도 구할 수 있음

print(answer if answer != MAX else -1)