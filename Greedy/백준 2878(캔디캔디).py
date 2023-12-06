import sys

m, n = map(int, input().split())
lst = [int(sys.stdin.readline()) for _ in range(n)]
t = sum(lst) - m # 부족한 개수
lst.sort()
answer = 0

for i in range(n):
    temp = t//(n-i) # 부족한 개수에서 남은 사람의 수를 나눈다
    if temp <= lst[i]: # 필요한 개수보다 줄 수 있는 개수가 작다면
        answer += (temp)**2 # 줄 수 있는 개수 만큼의 분노가 생김
        t -= temp
    else: # 필요한 개수보다 줄 수 있는 개수가 크다면
        answer += (lst[i])**2 # 필요한 개수 만큼 분노가 생김
        t -= lst[i]
print(answer%(2**64))