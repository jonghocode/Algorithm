import sys

def dfs(x, d):
    if d == 4:
        print("1")
        sys.exit(0)
    for i in dict[x]:
        if chk[i] == 0:
            chk[i] = 1
            dfs(i, d+1)
            chk[i] = 0



n, m = map(int, input().split())
dict = {i : [] for i in range(n)}
chk = [0]*n

for i in range(m):
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)

for i in range(n):
    dfs(i, 0)

print("0")