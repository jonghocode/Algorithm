# 1389번 케빈 베이컨의 6단계 법칙

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
    a, b = map(int, input().split())
    MAP[a][b] = 1
    MAP[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            MAP[i][j] = min(MAP[i][j], MAP[i][k] + MAP[k][j])

answer = MAX
for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        sum += MAP[i][j]
    if answer > sum:
        answer = sum
        sw = i

print(sw)