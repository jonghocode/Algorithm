# 크루스칼 ? -> 계속 최소의 도로만 잇는다.(union-find)

import sys
input = sys.stdin.readline

def find(idx):
    if root[idx] == idx:
        return root[idx]
    root[idx] = find(root[idx])
    return root[idx]

n, m = map(int, input().split())
graph = []
answer, cnt = 0, 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
    answer += c

root = [i for i in range(n+1)]
graph.sort(key = lambda x : x[2])

for a, b, e in graph:
    n1, n2 = find(a), find(b)
    if n1 != n2:
        root[n2] = n1
        answer -= e
        cnt += 1
    
    if cnt == n-1:
        break

print(answer if cnt == n-1 else -1)