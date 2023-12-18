def solution(msg):
    answer = []
    dict = {}; cnt = 0
    
    for i in range(1, 27):
        dict[chr(cnt + ord('A'))] = i; cnt += 1

    st = 0
    while st < len(msg):
        if st >= len(msg): # 인덱스 넘으면 종료
            break
        tempstr = '' # 사전 추가 할 문자열
        while st < len(msg):
            tempstr += msg[st]
            if tempstr not in dict: # 사전추가
                cnt += 1; dict[tempstr] = cnt;
                answer.append(dict[tempstr[:-1]])
                break
            st += 1
            if st >= len(msg): # 인덱스가 끝이라면
                answer.append(dict[tempstr]) # 이때까지 더한 문자열 출력 -> 끝나지 않았다면 딕셔너리에 있다는 뜻
                break
    
    return answer