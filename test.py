def chk(v, mid, arr):
    if len(arr) == 0: return False
    for cmp in arr:
        t = 0
        for i in range(mid):
            if word[v + i] != word[cmp + i]:
                t = 1
                break
        if t == 0:
            return True
    return False

X = 50001
n = int(input())
word = [0] + list(input())
l, r = 1, n
ans = 0
while l <= r:
    mid = (l + r) // 2
    hash = [[] for _ in range(X)]
    tmp, k, sw = 0, 1, 0
    for i in range(1, n + 1):
        if i < mid: k = (k * 31) % X
        if i > mid: 
            tmp = (ord(word[i - mid]) * k) % X
            tmp = (tmp + X) % X
        tmp = ((tmp*31) + ord(word[i])) % X
        if i >= mid:
            if chk(i - mid + 1, mid, hash[tmp]):
                sw = 1
                break
            hash[tmp].append(i - mid + 1)
    
    if sw == 1:
        l = mid + 1
        ans = max(ans, mid)
    else:
        r = mid - 1
print(ans)
