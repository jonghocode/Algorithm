import sys

def find(num):
    if num == root[num]:
        return root[num]
    root[num] = find(root[num])
    return root[num]

n, m = map(int, input().split())
root = [i for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        n1 = find(b)
        n2 = find(c)
        if n1 != n2:
            root[n2] = root[n1]
    else:
        if find(b) == find(a):
            print("YES")
        else:
            print("NO")
print(root)