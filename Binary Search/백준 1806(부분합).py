# 처음에 리스트 제일 앞에 0을 붙이지 않았더니 81%에서 틀렸습니다가 계속 떴다.
# 그 이유는 리스트 맨 처음 값이 답이 되는 경우이다.
# 처음에 0을 넣지 않으면 for문에서 처음의 값을 구하지 못하기 때문에 답이 나오지 않는다.

n, s = map(int, input().split())
lst = [0] + list(map(int, input().split()))
for i in range(2, n+1): # 누적합 이용
    lst[i] += lst[i-1]

l, r = 1, n+1
answer = 0x7fffffff

while l <= r:
    mid = (l + r) // 2
    flag = False
    
    for i in range(mid, n+1):
        if lst[i] - lst[i-mid] >= s:
            flag = True
            break
    
    if flag == True: # 합이 만들어진다면 구간 줄이기
        answer = min(answer, mid)
        r = mid - 1
    else: # 구간 늘리기
        l = mid + 1

if answer == 0x7fffffff: # 못 구하는 경우
    answer = 0
print(answer)