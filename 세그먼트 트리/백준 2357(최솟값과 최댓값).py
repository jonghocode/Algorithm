import sys
input = sys.stdin.readline
MAX = int(1e12)

def update(idx, l, r): # 세그먼트 트리 만들기
    if l == r:
        tree[idx] = (arr[l], arr[l]) # 초기화
        return tree[idx]

    mid = (l + r) // 2

    left = update(idx*2, l, mid)
    right = update(idx*2+1, mid+1, r)

    tree[idx] = (min(left[0], right[0]), max(left[1], right[1])) # 왼쪽은 최소, 오른쪽은 최대
    return tree[idx]

def query(l, r, idx):
    if r < a or b < l: # 범위를 벗어난다면
        return (MAX, 0)
    
    mid = (l + r) // 2

    if a <= l and r <= b: # 둘 다 범위에 들어온다면
        return tree[idx]
    else:
        left = query(l, mid, idx*2)
        right = query(mid+1, r, idx*2+1)
        return (min(left[0], right[0]), max(left[1], right[1]))

n, m = map(int, input().split())
cnt, h = 1, 1
while cnt <= n: # 세그먼트 트리 범위 구하기
    cnt *= 2
    h += 1
arr = [int(input()) for _ in range(n)]
tree = [0 for _ in range(1 << h)]
update(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    result = query(0, n-1, 1)
    print(*result)