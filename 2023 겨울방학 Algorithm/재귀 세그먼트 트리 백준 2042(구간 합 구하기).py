# update 내가 원하는 번호에 찾아들어가서 바꾸고 RETURN
# 합 구하기 -> 원하는 범위에 완전히 포함되면 취한다. 포함되지 않으면 들어감

import sys

def dfs(l, r):
    global d
    if l == r:
        dict[(l, r)] = d
        d += 1
        return
    dict[(l, r)] = d
    d += 1
    dfs(l, (l + r)//2)
    dfs((l+r)//2 + 1, r)

def update(l, r, num):
    if l == r:
        tree[dict[(l, r)]] = num
        return
    if (l + r) // 2 >= num:
        update(l, (l + r) // 2, num)
        tree[dict[(l, r)]] = tree[dict[(l, (l + r) //2)]] + tree[dict[((l + r) //2+1, r)]]
    if (l + r) // 2 + 1 <= num:
        update((l + r) // 2 + 1, r, num)
        tree[dict[(l, r)]] = tree[dict[(l, (l + r) //2)]] + tree[dict[((l + r) //2+1, r)]]
n, m, k = map(int, input().split())

st = 1; h = 0
while st <= n:
    st *= 2
    h += 1

d = 1
dict = {}
tree = [0 for _ in range(st*2)]
dfs(1, n)

for _ in range(n):
    d = 1
    num = int(sys.stdin.readline())
    update(1, n, num)
print(tree)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(1, n, c)
        pass
    else:
        # b ~ c까지 합
        pass
print(tree)