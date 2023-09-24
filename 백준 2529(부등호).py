n = int(input())
s = list(map(str, input().split()))
lst = []
chk = [0]*10
answer = []

def back(d):
    global n

    if d > 1:
        if s[d-2] == '>':
            if lst[d-2] <= lst[d-1]:
                return
        elif s[d-2] == '<':
            if lst[d-2] >= lst[d-1]:
                return
    if d == n+1: # 두번째로 한 방법(answer에 저장 한 후 마지막에 정렬 후 답 출력)
        answer.append(lst[:])
        return

    # if d == n+1: # 첫번째로 한 방법
    #     answer = ''
    #     for i in range(d):
    #         answer += str(lst[i])

    #     if int(answer) > int(answermax):
    #         answermax = answer
    #     if int(answer) < int(answermin):
    #         answermin = answer
     
    #     return

    for i in range(10):
        if chk[i] == 0:
            lst.append(i)
            chk[i] = 1
            back(d+1)
            lst.pop()
            chk[i] = 0
back(0)
answer.sort()
print(''.join(map(str, answer[-1])))
print(''.join(map(str, answer[0])))
# print(answermax)
# print(answermin)
