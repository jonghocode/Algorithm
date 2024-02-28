# 1865번 웜홀
import sys
input = sys.stdin.readline

TEST = int(input())
MAX = int(1e12)
for _ in range(TEST):
    n, m, w = map(int, input().split())
    dis = [MAX for _ in range(n+1)]
    graph = []
    for i in range(m):
        a, b, c = map(int, input().split())
        graph.append((a, b, c))
        graph.append((b, a, c))
    for i in range(w):
        a, b, c = map(int, input().split())
        graph.append((a, b, -c))
    
    for i in range(1, n+1):
        sw = 0
        for temp in graph:
            a, b, c = temp
            if dis[b] > dis[a] + c:
                sw = 1
                dis[b] = dis[a] + c
    
    print("NO" if sw == 0 else "YES")