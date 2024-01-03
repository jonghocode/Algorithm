import sys
from heapq import heappush, heappop

n = int(input())
MIN, MAX = [], [] # 최대힙, 최소힙
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(MIN) == len(MAX):
        if MAX and MAX[0] < num: # 최댓값보다 지금 들어온 값이 더 크면
            heappush(MIN, -heappop(MAX))
            heappush(MAX, num)
        else:
            heappush(MIN, -num)
    elif -MIN[0] > num: # 최솟값보다 더 작으면
        heappush(MAX, -heappop(MIN))
        heappush(MIN, -num)
    else: # 최솟값보다 더 크면
        heappush(MAX, num)
    print(-MIN[0])