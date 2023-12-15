def solution(number, k):
    stack = []
    n = len(number)
    k = n-k # 스택의 최대 길이
    for i in range(len(number)):
        if len(stack) == 0: # 0이면 무조건 넣기
            stack.append(number[i])
        else:
            if stack[-1] >= number[i] and len(stack) < k: # stack의 마지막 값보다 현재값이 작거나 같고 아직 더 넣어야한다면 넣기
                stack.append(number[i])
            elif stack[-1] < number[i]: # 크다면 빼야함
                while len(stack) != 0:
                    if stack[-1] >= number[i] or len(stack)+n-i <= k: # 값 비교 or 스택에 넣을 수 있는 길이가 k와 같거나 작아지면 break
                        break
                    stack.pop()
                stack.append(number[i]) # 현재 수 넣어주기
        
    return ''.join(map(str, stack))