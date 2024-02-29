# 1507번 궁금한 미호
# 이 문제는 플로이드의 결과값을 받은 후에 그걸 역으로 다시 바꾸는 문제이다.

import sys
input = sys.stdin.readline

N = int(input())
MAX = int(1e12)
MAP = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
sw = 0
for k in range(N):
    for i in range(N):
        if k == i:
            continue
        for j in range(N):
            if i == j:
                continue
            if k == j:
                continue
            if MAP[i][j] == MAP[i][k] + MAP[k][j]: # 다리를 없앤다
                visit[i][j] = 1
            elif MAP[i][j] > MAP[i][k] + MAP[k][j]: # 원래 있는 값이 더 크다면 최솟값이 아님
                print(-1)
                exit()

answer = 0
chk = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if chk[i][j] or visit[i][j] == 1:
            continue
        answer += MAP[i][j]
        chk[i][j] = 1; chk[j][i] = 1
print(answer)