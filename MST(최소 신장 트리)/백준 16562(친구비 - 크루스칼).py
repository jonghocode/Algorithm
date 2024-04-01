# mst는 프림과 크루스칼로 구현 가능
# 크루스칼 -> union-find

import sys
input = sys.stdin.readline

def find(idx):
    if root[idx] == idx:
        return root[idx]
    root[idx] = find(root[idx])
    return root[idx]

n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
root = [i for i in range(n+1)]

for _ in range(m):
    v, w = map(int, input().split())
    n1, n2 = find(v), find(w)
    if n1 != n2:
        if cost[v] > cost[w]:
            root[n1] = n2
            cost[n2] = min(cost[n2], cost[n1])
        else:
            root[n2] = n1
            cost[n1] = min(cost[n2], cost[n1])

ans = 0
for i in range(1, n+1):
    if find(i) == i: # 자신의 부모를 찾기위해서는 root[i]로 찾지말고 find로 찾아야함
        ans += cost[i]

print(ans if ans <= k else "Oh no")