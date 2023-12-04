import sys
from heapq import heappush, heappop

n = int(input())
lst = []
heap = []
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    lst.append([b, c])
lst.sort()
heappush(heap, lst[0][1])
print(lst)
for i in range(1, n):
    st, ed = lst[i][0], lst[i][1]
    ted = heappop(heap)
    if  st >= ted:
        heappush(heap, ed)
    else:
        heappush(heap, ed)
        heappush(heap, ted)

print(len(heap))