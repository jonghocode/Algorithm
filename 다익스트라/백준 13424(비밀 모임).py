from heapq import heappush, heappop
import sys
input = sys.stdin.readline
MAX = int(1e12)

TEST = int(input())
for _ in range(TEST):
    n, m = map(int, input().split())
    graph = {i : [] for i in range(1, n+1)}
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    k = int(input())
    f = list(map(int, input().split()))

    result = MAX
    for i in range(1, n+1):
        q = []
        dis = [MAX for _ in range(n+1)]
        heappush(q, (0, i))
        dis[i] = 0

        while q:
            sum, now = heappop(q)

            if dis[now] < sum:
                continue

            for e, w in graph[now]:
                if dis[e] > dis[now] + w:
                    dis[e] = dis[now] + w
                    heappush(q, (dis[now] + w, e))
        
        sum = 0
        for temp in f:
            sum += dis[temp]

        if result > sum:
            answer = i
            result = sum
    
    print(answer)