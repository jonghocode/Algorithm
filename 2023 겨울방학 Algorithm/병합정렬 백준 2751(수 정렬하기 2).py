import sys

def merge(l, r):

    if l == r:
        return
    
    merge(l, (l+r)//2)
    merge((l+r)//2 + 1, r)
    ls, le, rs, re = l, (l+r)//2, (l+r)//2 +1, r
    temp = []
    while ls <= le and rs <= re:
        if lst[ls] < lst[rs]:
            temp.append(lst[ls])
            ls += 1
        else:
            temp.append(lst[rs])
            rs += 1

    if ls <= le:
        for i in range(ls, le+1):
            temp.append(lst[i])
    else:
        for i in range(rs, re+1):
            temp.append(lst[i])

    idx = l
    for i in range(len(temp)):
        lst[idx + i] = temp[i]

n = int(input())
lst = [int(sys.stdin.readline()) for _ in range(n)]
merge(0, n-1)
print(*lst)