from heapq import heappush, heappop, heapify
test = int(input())
for _ in range(test):
    int(input())
    q = list(map(int, input().split()))
    heapify(q)
    answer = 0
    while True:
        x, y = heappop(q), heappop(q)
        answer += x+y
        if len(q) == 0:
            break
        heappush(q, x+y)
    print(answer)