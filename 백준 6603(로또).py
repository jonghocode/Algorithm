def dfs(lst, answer, d, p):
    if d == 6:
        for i in range(d):
            print(answer[i], end=" ")
        print()
        return
    for i in range(p, len(lst)):
        if chk[i] == 0:
            chk[i] = 1
            answer.append(lst[i])
            dfs(lst,answer,d+1,i+1)
            chk[i] = 0
            answer.pop(-1)


while(True):
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break
    chk = [0]*48
    answer = []
    dfs(lst, answer, 0,1)
    print()