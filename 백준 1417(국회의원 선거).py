import heapq
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

k = lst[0]
lst.pop(0)

q = []
for i in range(n-1):
    heapq.heappush(q, -lst[i])

answer = 0
if q:
    while True:
        if -q[0] < k:
            break
        z = -heapq.heappop(q)
        answer += 1
        z-=1
        k+=1
        heapq.heappush(q, -z)


print(answer)