def solution(plans):
    answer = []
    
    for i in range(len(plans)):
        word = plans[i][1]
        minute = int(word[:2])*60
        minute += int(word[3:])
        plans[i][1] = minute
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key = lambda x : x[1])
    
    idx = 1
    stack = [[plans[0][0], plans[0][1], plans[0][2]]]
    
    sw = 0
    while stack:
        a, b, c = stack.pop()
        if idx >= len(plans):
            sw = 1
        print(a, b, c, stack)
        if idx < len(plans):
            if b + c <= plans[idx][1]:
                answer.append(a)
                stack.append([plans[idx][0], plans[idx][1], plans[idx][2]])
            else:
                stack.append([a, plans[idx][1], c - (plans[idx][1] - b)])
                stack.append([plans[idx][0], plans[idx][1], plans[idx][2]])
    
        elif idx >= len(plans):
            answer.append(a)
        if sw == 0:
            idx += 1
    
    return answer
