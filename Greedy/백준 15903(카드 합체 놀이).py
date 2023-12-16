from heapq import heappush, heappop, heapify

n, m = map(int, input().split())
q = list(map(int, input().split()))
heapify(q)

for i in range(m):
    a, b = heappop(q), heappop(q)
    heappush(q, a+b)
    heappush(q, a+b)

print(sum(q))