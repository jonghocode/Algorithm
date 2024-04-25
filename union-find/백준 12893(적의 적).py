# 백준 12893(적의 적) : union-find

import sys
input = sys.stdin.readline

def find(idx):
    if root[idx] == idx:
        return root[idx]
    root[idx] = find(root[idx])
    return root[idx]

def join(p1, p2):
    n1, n2 = find(p1), find(p2)
    if n1 == n2:
        return
    root[n2] = n1

n, m = map(int, input().split())
graph = []
root = [i for i in range(n+1)]
enemy = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph.append((a, b))
    n1, n2 = find(a), find(b)
    if n1 == n2:
        print(0)
        exit()
    aenemy, benemy = enemy[a], enemy[b]

    if aenemy != 0:
        join(aenemy, b)
    else:
        enemy[a] = b
    
    if benemy != 0:
        join(benemy, a)
    else:
        enemy[b] = a

print(1)