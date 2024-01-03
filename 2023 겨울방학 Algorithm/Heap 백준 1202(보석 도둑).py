import sys
from heapq import heappush, heappop

n, k = map(int, input().split())
heap = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    heap.append([a, b])
lst = [int(sys.stdin.readline()) for _ in range(k)]
lst.sort(); heap.sort()
answer = 0
temp = [] # 정답이 들어가는 리스트

for i in lst:
    while heap and heap[0][0] <= i: # 가방의 무게가 더 커질 때 까지 보석 최대힙으로 넣기
        heappush(temp, -heap[0][1])
        heappop(heap)
    if temp: # 가장 가치가 높은 보석이 맨 앞에 들어가있음
        answer -= heappop(temp)
print(answer)