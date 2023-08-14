# 감소하면 감소한 값으로 값 초기화, cnt = 1
# 같거나 증가하면 값 더해주고 cnt+1

t = int(input()) # 테스트케이스 수

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    answer, st = 0, lst[0]
    
    for i in range(1, n):
        if st >= lst[i]:
            answer += st-lst[i]
        else:
            st = lst[i]
    print(answer)