# 소수의 연속합(투포인터, 에레토스테네스의 체)
# 처음 두개의 포인터 st, ed는 0번 인덱스에서 시작해서
# ed는 출발한다. n을 넘으면 ed는 그만 움직인다.
# 그리고 st출발한다. 현재 값이 n보다 작아지면 멈추고
# n과 같다면 답 체크 후 ed 이동

n = int(input())
arr = [True] * (n+1)
m = int(n ** 0.5)
for i in range(2, m + 1):
    if arr[i] == True:         
        for j in range(2*i, n+1, i):
            arr[j] = False
lst = [i for i in range(2, n+1) if arr[i] == True] # 소수 미리 구해놓기

st, ed, sum, answer = -1, -1, 0, 0

while len(lst) > ed:
    if sum < n: # 현재 값이 n보다 작다면 ed 이동
        ed += 1
        if ed == len(lst): 
            break
        sum += lst[ed]
    else:
        if sum == n: # n과 같다면 답 체크
            answer += 1
        st += 1
        sum -= lst[st]
        
print(answer)