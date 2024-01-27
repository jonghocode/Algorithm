import sys

n = int(input())
w = [0]
graph = {i : [] for i in range(n+1)}
depth = [-1 for _ in range(n+1)]
for _ in range(n):
    w.append(int(sys.stdin.readline()))

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))