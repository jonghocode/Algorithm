# chk배열 x <- 10**9라서
from heapq import heappush, heappop
import sys

n, m = map(int, input().split())
lst = list(map(int, input().split()))
temp = list(lst)
lst.sort(reverse=True)

q = []
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    heappush(q, [a, b])



before, cnt, answer, answer2 = -1, 0, 0, 0
while q:
    st, ed = heappop(q)
    if st != before:
        cnt = 0
        answer += lst[cnt]
        answer2 += temp[cnt]
        before = st
        if st < ed:
            if q[0][0] > 
            heappush(q, [st+1, ed])
    else:
        cnt += 1
        answer += lst[cnt]
        answer2 += temp[cnt]
        if st < ed:
            heappush(q, [st+1, ed])
        before = st




print(answer2, answer)