import sys
from collections import defaultdict

def find(x):
    if root[x] == x:
        return root[x]
    root[x] = find(root[x])
    return root[x]

n = int(input())
m = int(input())
E, F = [], []

for _ in range(m):
    k = list((sys.stdin.readline().strip().split()))
    a, b = int(k[1]), int(k[2])
    if k[0] == 'E':
        E.append((a, b))
        E.append((b, a))
    else:
        F.append((a, b))
        F.append((b, a))

root = [i for i in range(n+1)]
for st, ed in F:
    a, b = find(st), find(ed)
    if a != b:
        root[b] = a

print(root)