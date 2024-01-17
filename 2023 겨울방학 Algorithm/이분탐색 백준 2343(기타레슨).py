n, m = map(int, input().split())
lst = list(map(int, input().split()))

l, r = 1, sum(lst)
answer = int(1e12)
while l <= r:
    mid = (l + r) // 2
    
    ans, cnt, sw = 0, 1, 0
    for i in range(n):
        if lst[i] > mid:
            sw = 1
            break
        if ans + lst[i] <= mid:
            ans += lst[i]
        else:
            ans = lst[i]
            cnt += 1
    
    if sw == 1:
        l = mid + 1
        continue
    if cnt <= m:
        answer = min(answer, mid)
        r = mid - 1
    else:
        l = mid + 1

print(answer)