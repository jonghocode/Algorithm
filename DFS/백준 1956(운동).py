import sys

v, e = map(int, input().split())
answer = 0x7fffffff
visit = [[0x7fffffff for _ in range(v+1)] for _ in range(v+1)]

# 플로이드 워셜 알고리즘 배열 초기화
for i in range(v+1):
    for j in range(v+1):
        if i == j:
            visit[i][j] = 0

for i in range(e):
    lst = list(map(int, sys.stdin.readline().strip().split()))
    visit[lst[0]][lst[1]] = lst[2] # 인접행렬 그래프 생성

# 플로이드 워셜 알고리즘 기본 틀
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            visit[i][j] = min(visit[i][j], visit[i][k] + visit[k][j])
    
for i in range(1, v+1):
    for j in range(1, v+1):
        if i == j: continue
        answer = min(answer, visit[i][j] + visit[j][i])
if answer == 0x7fffffff: answer = -1
print(answer)