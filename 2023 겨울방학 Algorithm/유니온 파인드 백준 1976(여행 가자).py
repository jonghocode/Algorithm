import sys

def find(x):
    if root[x] == x:
        return root[x]
    root[x] = find(root[x])
    return root[x]

n = int(input())
m = int(input())
edge = []
root = [i for i in range(n)]
for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if lst[j] == 1:
            edge.append((i, j))

edge.sort()
trip = set(list(map(int, input().split())))

for a, b in edge:
    n1, n2 = find(a), find(b)
    if n1 != n2:
        root[n2] = n1

trip = list(trip)

for i in range(n):
    find(i)

for i in range(len(trip)-1):
    if root[trip[i]-1] != root[trip[i+1]-1]:
        print("NO")
        exit()
print("YES")