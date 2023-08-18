n = int(input())
chk = [0]*26
lst = []
for i in range(n):
    lst.append(list(map(str, input())))

for i in range(n):
    st = 1
    for j in range(len(lst[i])-1, -1, -1):
        chk[ord(lst[i][j])-ord('A')] += st
        st*=10

answer, st = 0, 9
chk.sort(reverse=True)
for i in chk:
    answer += i*st
    st -= 1

print(answer)