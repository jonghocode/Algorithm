def chkWord(now, mid, arr):
    if len(arr) == 0: return False  # 해당 키에 값이 없으면 False
    for cmp in arr:
        tmp = 0
        for i in range(mid):  # 키의 값들 중 다른 값이 있으면 
            if word[now + i] != word[cmp + i]:
                tmp = 1
                break
        if tmp == 0: return True
    return False

X = 50001
n = int(input())
word = [0] + list(input())
l, r = 1, n
ans = 0
while l <= r:
    mid = (l + r) // 2
    hash = [[] for _ in range(X)]
    tmp, k, flag = 0, 1, 0
    for i in range(1, n + 1):
        if i < mid : k = (k * 31) % X  # 맨 앞글자를 빼기 위한 k값 계산(31^3 -> 31^0 처럼 떨어지는 구조)
        if i > mid:
            tmp -= (ord(word[i - mid]) * k) % X  # 맨 앞글자 빼기
            tmp = (tmp + X) % X  # 음수 나오지 않게 치환
        tmp = (tmp * 31 + ord(word[i])) % X  # 한글자씩 추가
        if i >= mid:
            if chkWord(i - mid + 1, mid, hash[tmp]):
                flag = 1
                break
            hash[tmp].append(i - mid + 1)
    if flag == 1:
        ans = max(ans, mid)
        l = mid + 1
    else:
        r = mid - 1
    
print(ans)