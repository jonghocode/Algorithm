n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(key = lambda x : (x%10, x)) # 10으로 나누어 떨어지고 오름차순
answer, cnt = 0, 0
for i in lst:
    if i % 10 == 0: # 10으로 나누어 떨어지면 따로 처리
        if m-cnt >= i//10-1:
            answer += i//10 # answer이 1개 더 많음
            cnt += i//10-1
        else:
            answer += m-cnt # 똑같이 더하기
            cnt += m-cnt
    else:
        if m-cnt <= i//10:
            answer += m-cnt
            cnt += m-cnt
        else:
            cnt += i//10
            answer += i//10
print(answer)