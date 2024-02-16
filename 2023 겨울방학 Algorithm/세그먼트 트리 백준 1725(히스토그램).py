import sys
sys.setrecursionlimit(10**5)

def MIN(x, y):
    return x if x[0] < y[0] else y

def findMin(l, r, st, ed, k):
    if l > ed or r < st:
        return [0x7fffffff, 0x7fffffff]
    if st <= l and r <= ed:
        return tree[k]
    mid = (l + r) // 2
    return MIN(findMin(l, mid, st, ed, k*2), findMin(mid+1, r, st, ed, k*2+1))

def process(l, r):
    global answer, t
    if l > r:
        return
    p = findMin(1, t, l, r, 1)
    answer = max(answer, p[0]*(r-l+1))

    process(l, p[1]-1)
    process(p[1]+1, r)

n = int(input())
tree = [[0x7fffffff, 0] for _ in range(1<<18)]

t = 1
while t <= n:
    t *= 2

for i in range(n):
    num = int(sys.stdin.readline())
    tree[t+i] = [num, i+1]
    temp = t+i
    temp //= 2

    while temp > 0:
        tree[temp] = MIN(tree[temp*2], tree[temp*2+1])
        temp //= 2

answer = 0

process(1, n)
print(answer)