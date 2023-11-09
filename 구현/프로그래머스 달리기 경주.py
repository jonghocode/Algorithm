# 이름이 키인 딕셔너리와 순위가 키인 딕셔너리 사용
# 키를 이용하면서 순서 바꿔주기
def solution(players, callings):
    answer = []
    name, num = {}, {}
    for i in range(len(players)):
        name[players[i]] = i+1
        num[i+1] = players[i]
        
    for command in callings:
        temp = name[command]
        if temp != 1:
            up = num[temp] # 올라가는 사람 이름
            down = num[temp-1] # 내려가는 사람 이름
            name[up] -= 1
            name[down] += 1
            num[temp] = down
            num[temp-1] = up
        
    lst = []
    for k, v in num.items():
        lst.append([k, v])
    lst.sort()
    for k, v in lst:
        answer.append(v)
    
        
    return answer
