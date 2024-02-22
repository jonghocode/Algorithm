def update(l, r, k, num):
    if num < l or num > r:
        return tree[k]
    if l == r:
        tree[k] = 1
        return tree[k]
    mid = (l + r) // 2
    tree[k] = update(l, mid, k*2, num) + update(mid+1, r, k*2+1, num)
    return tree[k]
    
def query(l, r, st, ed, k):
    if ed < l or r < st:
        return 0
    if st <= l and r <= ed:
        return tree[k]
    mid = (l + r) // 2
    return query(l, mid, st, ed, k*2) + query(mid+1, r, st, ed, k*2+1)

n = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
answer = 0
dict = {}
for i in range(1, n+1):
    dict[A[i]] = i

t = 1; cnt = 0
while t <= n:
    t *= 2
    cnt += 1

tree = [0 for _ in range(1<<(cnt+1))]
for i in range(1, n+1):
    answer += query(1, t, dict[B[i]], t, 1)
    update(1, t, 1, dict[B[i]])

print(answer)