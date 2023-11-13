def solution(n):
    answer = 0
    st, ed = -1, -1
    lst = [i for i in range(1, n+1)]
    sum = 0

    while ed < n-1:
        if sum < n:
            ed += 1
            sum += lst[ed]
        else:
            if sum == n:
                answer += 1
            st += 1
            sum -= lst[st]



    return answer+1
