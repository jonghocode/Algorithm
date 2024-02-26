# 다이나믹, 사이클 확인 가능, 음수(V*E)
# v-1번 경화, 1번 경화
import sys

n, m = map(int, input().split())
MAX = int(1e12)
lst = [MAX for _ in range(n+1)]; lst[1] = 0
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

for _ in range(n-1):
    for i in range(m):
        a, b, c = graph[i][0], graph[i][1], graph[i][2]
        if lst[a] + c < lst[b]:
            lst[b] = lst[a] + c

temp = list(lst)
for i in range(m):
    a, b, c = graph[i][0], graph[i][1], graph[i][2]
    if lst[a] + c < lst[b]:
        lst[b] = lst[a] + c

answer = []; sw = 0

for i in range(2, n+1):
    if lst[i] == MAX:
        answer.append(-1)
    if lst[i] != temp[i]:
        print(-1)
    elif lst[i] == temp[i]:
        sw = 1
        answer.append(lst[i])
print(lst)
print(temp)
if sw == 0:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i])