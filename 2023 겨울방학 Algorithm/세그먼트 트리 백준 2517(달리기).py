import sys
sys.setrecursionlimit(10**5)

def query(l, r, st, ed, k):
    if st <= l and r <= ed: # 범위에 다 포함된다면
        return tree[k]
    if l > ed or r < st: # 범위를 벗어난다면
        return 0
    mid = (l + r) // 2
    return query(l, mid, st, ed, k*2) + query(mid + 1, r, st, ed, k*2 + 1)

def update(l, r, d, k):
    if l > d or r < d: # 범위를 벗어난다면
        return tree[k]
    if l == d and r == d: # 끝까지 도착했다면
        tree[k] = 1
        return tree[k]
    mid = (l + r) // 2
    tree[k] = update(l, mid, d, k*2) + update(mid + 1, r, d, k*2 + 1) # 값 바꾸기
    return tree[k]

n = int(input())
arr = [[0, 0]]
for i in range(n):
    arr.append([int(sys.stdin.readline()), i])
arr.sort(key = lambda x : x[0]) # 값의 압축
for i in range(n+1):
    arr[i][0] = i
arr.sort(key = lambda x : x[1])

tree = [0]*(n*2+1)
for i in range(1, n+1):
    print(query(1,n,arr[i][0]+1,n,1) + 1)
    update(1, n, arr[i][0], 1)