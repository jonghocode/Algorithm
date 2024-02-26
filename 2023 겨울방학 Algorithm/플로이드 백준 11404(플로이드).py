# 11404번 플로이드(O)
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
MAX = int(1e12)
MAP = [[MAX for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            MAP[i][j] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    MAP[a][b] = min(MAP[a][b], c)

for k in range(1, n+1): # k를 경유해서 갈 때
    for i in range(1, n+1):
        for j in range(1, n+1):
            MAP[i][j] = min(MAP[i][j], MAP[i][k] + MAP[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(MAP[i][j] if MAP[i][j] != MAX else 0, end = ' ')
    print()