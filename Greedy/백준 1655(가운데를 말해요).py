from heapq import heappush, heappop

n = int(input())
mid = int(input())
maxq, minq = [], []
print(mid)

for i in range(n-1):
    k = int(input())
    
    a, b = max(mid, k), min(mid, k)
    heappush(maxq, -b)
    heappush(minq, a)

    if len(maxq) != len(minq):
        if len(maxq)> len(minq):
            mid = -heappop(maxq)
        else:
            mid = heappop(minq)
    else:
        mid = -heappop(maxq)
    print(mid)
            