n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda x : (x[1], -x[0]))
chk = [0]*10001

#for i in range(n):
#    print("p : %d  d : %d" % (lst[i][0], lst[i][1]))

for i in range(n):
    if chk[lst[i][1]] == 0:
        chk[lst[i][1]] = lst[i][0]
    else :
        sw = 0
        m = 98765
        st = -1
        for j in range(1, lst[i][1]):
           # 앞에 있는 값 중 최솟값 찾기
            if m > chk[j]:
                m = chk[j]
                st = j
        if sw == 0 and st!= -1 and chk[st] < lst[i][0]: # 그 최솟값보다 현재값이 더 크면 현재값 넣기
            chk[st] = lst[i][0]

answer = 0
for i in range(10001):
    answer+=chk[i]
print(answer)
