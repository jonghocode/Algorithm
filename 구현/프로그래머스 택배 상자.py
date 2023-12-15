def solution(order):
    answer = 0
    idx = 1
    stack = []
    
    while idx < len(order)+1:
        stack.append(idx)
        while len(stack) and stack[-1] == order[answer]: # main부분이 남아있거나 주문과 똑같다면 빼기
            answer += 1
            stack.pop()
        idx += 1 # 다음 상자
    return answer