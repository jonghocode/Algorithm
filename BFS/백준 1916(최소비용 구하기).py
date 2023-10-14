import sys
from collections import deque

n = int(input())
graph = {i:[] for i in range(1, n+1)}
dp = [0x7fffffff]*(n+1)

for i in range(int(input())):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append([b, c])

start, end = map(int, input().split())

q = deque([])
q.append([start, 0])
dp[start] = 0

while q:
    num, money = q.popleft()
    if money > dp[num]:
        continue
    for i in range(len(graph[num])):
        city, cost = graph[num][i][0], graph[num][i][1]
        if dp[city] > cost + money:
            dp[city] = cost + money
            q.append([city, cost + money])

print(dp[end])