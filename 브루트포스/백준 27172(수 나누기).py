# n <= 100,000 -> nlog(n) or 그리디 or 투포인터
# 이 문제는 그리디(힙 사용 x)

# 에라토스테네스의 체 처럼 문제 풀기(자신의 배수에 있는 것을 다 체크)
# 처음에 이 방법을 생각했었는데 최악의 경우를 생각했을 때 당연히 안될것같아서
# 다른 방법을 찾아보다가 풀이를 봤는데 이 방식의 시간복잡도가 nlog(n) 이라는 것을 알았다..

n = int(input())
lst = list(map(int, input().split()))
M = max(lst)
chk = [0 for _ in range(M+1)]

for i in lst:
    chk[i] = 1

answer = [0 for _ in range(M+1)]

for i in lst:
    cnt = 2
    while True:
        if i*cnt > M:
            break
        if chk[i*cnt] == 1:
            answer[i] += 1
            answer[i*cnt] -= 1
        cnt += 1
            
for i in lst:
    print(answer[i], end=' ')