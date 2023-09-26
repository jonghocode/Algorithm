n ,m, l = map(int, input().split())
t = []
if n != 0:
    lst = list(map(int, input().split()))
    lst.sort()
    t.append(lst[0]-1)
    for i in range(1, n):
        t.append(lst[i] - lst[i-1]-1)
    t.append(l - lst[n-1]-1)
    t.sort()
else:
    t.append(l-1)

le, ri = 1, l

while le <= ri:
    mid = (le+ri)//2
    sum = 0
    for i in t:
        sum += i//mid

    if sum > m:
        le = mid + 1
    else :
        ri = mid - 1

print(le)
