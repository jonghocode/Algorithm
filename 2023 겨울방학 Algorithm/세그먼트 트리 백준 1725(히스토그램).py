import sys

def update(l, r, idx, k):
    global num
    if idx < l or idx > r:
        return tree[k]
    if l == idx and r == idx:
        tree[k] = num
        return tree[k]
    mid = (l + r) // 2

    tree[k] = min(update(l, mid, idx, k*2), update(mid+1, r, idx, k*2+1))
    return tree[k]

n = int(input())
tree = [0]*(n*2+1)
for i in range(1, n+1):
    num = int(sys.stdin.readline())
    update(1, n, i, 1)
print(tree)