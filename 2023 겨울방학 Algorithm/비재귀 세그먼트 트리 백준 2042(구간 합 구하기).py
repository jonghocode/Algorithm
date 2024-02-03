import sys
n, m, k = map(int, input().split())
lst = [int(sys.stdin.readline()) for _ in range(n)]

st = 1; h = 0
while st <= n:
    st *= 2
    h += 1

tree = [0 for _ in range(st+n+3)]
for i in range(st, st+n+1):
    if i - st >= n:
        tree[i] = 0
    else:
        tree[i] = lst[i - st]
temp = st; ed = len(tree)
for i in range(h):
    for j in range(temp, ed-1, 2):
        print(temp, ed, j)
        tree[j//2] = tree[j] + tree[j+1]
    print(tree)
    ed = temp
    temp //= 2

print(tree)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        # b -> c
        pass
    else:
        # b ~ c까지 합
        pass
