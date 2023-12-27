# 백준 13397(구간 나누기 2)

n, m = map(int, input().split())
lst = list(map(int, input().split()))
l, r = 0, max(lst)
answer = r
while l <= r:
    mid = (l + r) // 2
    
    cnt = 1
    MIN, MAX = lst[0], lst[0]
    for i in range(n):
        MIN = min(MIN, lst[i])
        MAX = max(MAX, lst[i])
        if abs(MAX - MIN) > mid:
            cnt += 1
            MIN, MAX = lst[i], lst[i]

    if cnt <= m:
        answer = min(answer, mid)
        r = mid - 1 # 최솟값을 찾아야하기 때문
    else:
        l = mid + 1
    
print(answer)