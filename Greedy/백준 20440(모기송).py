import sys

n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))

lst.sort()
st, ed = lst[0][0], lst[0][1]

answer = -1
cnt = 1

for i in range(1, n):
    if st != lst[i][0]:
        if ed >= lst[i][0]:
            st = lst[i][0]
            cnt += 1
        else:
            if cnt > answer:
                a = st
                b = ed
                answer = cnt
            
            st = lst[i][0]
            ed = lst[i][1]
            cnt = 1
    else:
        ed = lst[i][1]
        cnt += 1
    print(st, ed, cnt)