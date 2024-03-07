def back(d, n, s, now):
    if d == n and sum(answer) == 0 and answer[0] > 0:
        temp.append(s)
        return
    if d >= n:
        return
    for i in range(now, n+1):
        answer.append(i)
        if s != '':
            back(d+1, n, s+'+'+str(i), i+1)
        else:
            back(d+1, n, s + str(i), i+1)
        answer.pop()

        answer.append(-i)
        if s != '':
            back(d+1, n, s+'-'+str(i), i+1)
        else:
            back(d+1, n, s+str(i), i+1)
        answer.pop()

        if answer:
            t = answer.pop()
            t*=10
            if t < 0:
                answer.append(t-i)
                back(d+1, n, s+' '+str(i), i+1)
            else:
                answer.append(t+i)
                back(d+1, n, s+' '+str(i), i+1)

            

t = int(input())
for _ in range(t):
    n = int(input())
    answer = []
    temp = []
    back(0, n, '', 1)
    temp.sort()
    for i in temp:
        print(i)
    print()
