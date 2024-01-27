import sys

def find(root, d):
    global num
    if root == -1:
        return
    find(graph[root][0][0], d+1)
    answer[d].append(num)
    num += 1
    find(graph[root][0][1], d+1)

n = int(input())
graph = {i : [] for i in range(n+1)}
chk = [0 for i in range(n+1)]
for i in range(n):
    k, l, r = map(int, sys.stdin.readline().split())
    graph[k].append((l, r))
    chk[l] = 1
    chk[r] = 1

for i in range(n):
    if chk[i] == 0:
        start = i

num = 1
answer = [[] for i in range(n+1)]

find(start, 1)
ans = 0
for i in range(1, n+1):
    if answer[i]:
        if ans <  max(answer[i]) - min(answer[i]) + 1:
            sw = i
            ans = max(answer[i]) - min(answer[i]) + 1
print(sw, ans)