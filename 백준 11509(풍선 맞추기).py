# 화살이 줄어드는 것을 chk 배열을 이용해서 줄어드는 것으로 했다.
n = int(input())
lst = list(map(int, input().split()))
arrow = [0]*1000001
answer = 0
for i in range(n):
    if arrow[lst[i]] == 0:
        answer += 1
        arrow[lst[i]-1]+=1
    else:
        arrow[lst[i]] -= 1
        arrow[lst[i]-1] += 1
    #print(arrow[1], arrow[2], arrow[3], arrow[4], arrow[5], answer)

print(answer)
