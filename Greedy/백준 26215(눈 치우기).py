import heapq

n = int(input())
lst = list(map(int, input().split()))
heap = []
for i in lst:
    heapq.heappush(heap, -i)
answer = 0
while heap:
    a, b = 1, 1
    a = heapq.heappop(heap)
    if heap :
        b = heapq.heappop(heap)
    
    if a != 1:
        a *= -1
        a -= 1
        if a != 0:
            heapq.heappush(heap, -a)
    if b != 1:
        b *= -1
        b -= 1
        if b != 0:
            heapq.heappush(heap, -b)
    answer += 1
if answer > 1440:
    answer = -1
print(answer)