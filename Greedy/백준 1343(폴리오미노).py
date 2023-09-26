s = input()
lst = []
answer = ''
for i in range(len(s)):
    if s[i] == '.':
        lst.append(i)
lst.append(len(s))

for i in range(len(lst)):
    if i == 0:
        t = lst[i]
    else:
        t = lst[i] - lst[i-1] -1

    if t % 4!=0 and t % 2!=0: # 아예 만들 수 없으면
        answer = '-1'
        break

    while t > 0:
        if t-4 >= 0:
            answer+='AAAA'
            t-=4
        elif t-2 >=0:
            t-=2
            answer+='BB'
    if i != len(lst)-1:
        answer+='.'

print(answer)
