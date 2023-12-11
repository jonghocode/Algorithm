import sys
from heapq import heappush, heappop

n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort()

q = [[0, 0]]
x, y, z = 0, 0, 0
for s, e in lst:
    if len(q) > 0 and q[0][0] <= s: # q의 끝나는 시간이 현재 시간보다 작거나 같다면
        heappop(q)
    heappush(q, [e, s])

    if y == 0 or len(q) == z and y == s: # 끝나는 시간 바꿔주기
        y = q[0][0]

    if len(q) > z: # 답 변경
        z = len(q)
        x = s
        y = q[0][0]

print(f"{z}\n{x} {y}")