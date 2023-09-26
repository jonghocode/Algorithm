# 자신보다 하나 아래에 있는 값에서 +1 한 값을 들고온다
# 마지막에 그 중 최댓값을 n에서 뺀다

n = int(input())
lst = list(map(int, input().split()))
chk = [0]*(n+1)
for i in range(n):
    chk[lst[i]] = chk[lst[i]-1] + 1
print(n-max(chk)) 
