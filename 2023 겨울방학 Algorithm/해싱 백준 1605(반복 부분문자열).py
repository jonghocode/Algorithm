def compare(v, w, mid, s):
    for i in range(mid):
        if s[v+i] != s[w+i]:
            return False
    return True

def fun(mid, s):

    answer, cnt = 0, 0
    st = ''
    for i in range(n):
        if i < mid:
            k = ord(s[i]) - ord('a') + 1
            answer += k*(r**cnt)
        
        else:
            k = ord(s[i-mid]) - ord('a') + 1
            answer = answer - (k*(r**(cnt-mid)))

        if i >= mid:
            for j in range(len(hash[answer])):
                if compare(hash[answer][j],i-mid+1,mid, s):
                    return True
            hash[answer].append(i-mid+1)

        cnt += 1
    return False

r, X = 31, 50007
hash = [[] for i in range(X)]
n = int(input())
s = input()
res = 0

l, r = 1, n
while l <= r:
    mid = (l + r) // 2
    if fun(mid, s):
        l += 1
        res = max(res, mid)
    else:
        r -= 1


print(res)
