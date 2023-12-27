n, m = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0x7fffffff
# 최댓값 - 최솟값을 mid 값으로 둔다
l, r = 0, max(lst) # l은 나올 수 있는 가장 작은 값, r은 가장 큰 값
while l <= r:
    mid = (l + r) // 2
    cnt = 1 # 하나는 무조건 있음

    MAX, MIN = lst[0], lst[0]
    for i in lst:
        MAX, MIN = max(MAX, i), min(MIN, i)
        if MAX - MIN > mid: # 최댓값 - 최솟값이 mid보다 크다면 구간 갯수 늘리기
            cnt += 1
            MAX, MIN = i, i
    
    if cnt <= m: # 답을 구할 수 있다면
        answer = min(answer, mid)
        r = mid - 1
    else:
        l = mid + 1

print(answer)