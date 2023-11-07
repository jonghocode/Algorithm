def solution(stones, k):
    answer = -1
    l, r = 0, max(stones)
    
    while l <= r:
        mid = (l + r) // 2
        cnt = 0 # 음수가 되는 개수 카운트 해야함
        for i in range(len(stones)):
            if cnt >= k:
                break
            if stones[i]-mid < 0:
                cnt += 1
            else:
                cnt = 0
        
        if cnt >= k:
            r = mid - 1
        else:
            l = mid + 1
            answer = max(answer, mid)

    return answer
