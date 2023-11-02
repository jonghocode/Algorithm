def solution(plans):

    for i in range(len(plans)):
        word = plans[i][1]
        minute = int(word[:2])*60
        minute += int(word[3:])
        plans[i][1] = minute
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key = lambda x : x[1])
    
    # plans의 앞에서부터 하나씩 뽑아서 검사
    now = plans.pop(0) # 작업 중인 과제
    time = now[1] # 현재 시간
    stack = [] # 중단한 과제
    answer = [] # 결과

    while plans:
        # 새로운 과제가 현재 작업 중인 과제가 끝나기 전에 시작한다면
        a, b, c = now[0], now[1], now[2]
        x, y, z = plans[0][0], plans[0][1], plans[0][2]
        
        if time + c > y:
            # 현재 과제를 중단한 과제에 넣고 새로운 과제 시작
            stack.append([a, b, c - (y - time)])
            now = plans.pop(0)
            time = now[1]
        else:
            # 현재 과제 종료
            time += now[2]
            answer.append(now[0])

            # 과제가 끝나자마자 새로운 과제가 시작하거나, 중단한 과제가 없다면 새로운 과제 시작
            if time == plans[0][1] or not stack:
                now = plans.pop(0)
                time = now[1]
            else:
                now = stack.pop()

    answer.append(now[0])
    
    for item in stack[::-1]:
        answer.append(item[0])
            
    return answer
