# update 내가 원하는 번호에 찾아들어가서 바꾸고 RETURN
# 합 구하기 -> 원하는 범위에 완전히 포함되면 취한다. 포함되지 않으면 들어감

import sys

def dfs(l, r, k): # 트리 생성
    if l == r: # 끝까지 갔다면
        tree[k] = num[l] # 트리에 기록
        return tree[k]
    
    mid = (l + r) // 2
    tree[k] = dfs(l, mid, k*2) + dfs(mid + 1, r, k*2 + 1) # 구간 합 생성
    return tree[k]

def update(l, r, k, b, c):
    if l > b or r < b: # 범위를 벗어난다면
        return tree[k]
    if l == r and b == l: # 업데이트 할 위치라면
        tree[k] = c
        return tree[k]
    
    mid = (l + r) // 2
    tree[k] = update(l, mid, k*2, b, c) + update(mid+1, r, k*2 + 1, b, c) # 합 변경
    return tree[k]

def query(l, r, k, b, c):
    if l > c or r < b: # 범위를 벗어난다면
        return 0
    if b <= l and r <= c: # 범위에 속한다면
        return tree[k]
    mid = (l + r) // 2
    return query(l, mid, k*2, b, c) + query(mid+1, r, k*2 + 1, b, c)

n, m, k = map(int, input().split())

st = 1; h = 0
while st <= n:
    st *= 2
    h += 1

d = 1
dict = {}
tree = [0 for _ in range(st*2)]
num = [0] + [int(sys.stdin.readline()) for _ in range(n)]

dfs(1, n, 1)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(1, n, 1, b, c)
    else:
        print(query(1, n, 1, b, c))