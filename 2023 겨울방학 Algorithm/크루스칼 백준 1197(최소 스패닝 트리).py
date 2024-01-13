import sys

def find(x):
    if root[x] == x:
        return root[x]
    root[x] = find(root[x])
    return root[x]

n, m = map(int, input().split())
answer, cnt = 0, 0
root = [i for i in range(n+1)]
edge = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edge.append((c, a, b))

edge.sort(key = lambda x : x[0])
for w, a, b in edge:
    n1, n2 = find(a), find(b)
    if n1 != n2:
        root[n2] = n1
        answer += w; cnt += 1
    
    if cnt == n-1:
        break

print(answer)