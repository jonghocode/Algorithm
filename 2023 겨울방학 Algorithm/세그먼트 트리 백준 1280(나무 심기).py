# 답 구해주고 트리에 갱신

import sys

def query(l, r, st, ed, k):
    if st <= l and r <= ed: # 범위가 완전히 포함된다면 값을 return
        return tree[k]
    if l > ed or r < st: # 범위를 벗어나면 0을 return
        return [0, 0]

    mid = (l + r) // 2
    left = query(l, mid, st, ed, k*2)
    right = query(mid+1, r, st, ed, k*2+1)
    
    return [left[0] + right[0], left[1] + right[1]]

def update(l, r, d, k):
    if l > d or r < d: # 범위를 벗어난다면 return
        return tree[k]
    if l == d and r == d:
        tree[k][0] += 1 # 개수 올려주기
        tree[k][1] += d # 값 올려주기
        return tree[k]
    
    mid = (l + r) // 2
    left = update(l, mid, d, k*2)
    right = update(mid+1, r, d, k*2+1)
    tree[k][0] = left[0] + right[0]
    tree[k][1] = left[1] + right[1]
    return tree[k]


n = int(input())
tree = [[0, 0] for _ in range(1<<19)]
answer = 1

for i in range(n):
    num = int(sys.stdin.readline())
    if i > 0:
        left = query(0, 200000, 0, num-1, 1)
        right = query(0, 200000, num+1, 200000, 1)
        temp = abs(left[0] * num - left[1]) + abs(right[0] * num - right[1])
        answer *= temp
        answer %= 1_000_000_007

    update(0, 200000, num, 1)

print(answer % 1_000_000_007)