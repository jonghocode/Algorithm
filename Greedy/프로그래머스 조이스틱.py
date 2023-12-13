def solution(name):
    answer = 0

    # ABCDEFGHIJKLM NOPQRSTUVWXYZ
    # M 까지 12
    # M 까지면 오른쪽으로 더해주기
    # 9 + 4 + 9 + 12 + 4 + 13 + 총 글자수 -1
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    new = ''
    for i in name:
        if i == 'A':
            continue
        new += i
        answer += lst[ord(i)-ord('A')]
    temp = len(new)
    cnt = 0
    for i in range(len(name)):
        if temp == 0:
            break
        if name[i] in new:
            temp -= 1
        cnt += 1
        
    temp = len(new)
    cnt2 = 0
    for i in range(len(name)-1, -1, -1):
        if temp == 0:
            break
        if name[i] in new:
            temp -= 1
        cnt2 += 1

    if cnt == cnt2:
        answer -= 1
    if len(new) == 2:
        answer -= 1
    return answer + min(cnt, cnt2)
    