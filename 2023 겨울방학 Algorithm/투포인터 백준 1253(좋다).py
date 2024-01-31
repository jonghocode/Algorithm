n = int(input())
lst = list(map(int, input().split()))
lst.sort()
answer = 0

for i in range(n):
    l, r = 0, n-1
    while l < r:
        k = lst[l] + lst[r]
        if l == i:
            l += 1
            continue
        elif r == i:
            r -= 1
            continue
        if k == lst[i]:
            answer += 1
            break
        elif k < lst[i]:
            l += 1
        else:
            r -= 1
print(answer)