def p(idx):
    if go[idx] == -1:
        # print(lst[go[idx]], end = ' ')
        return
    p(go[idx])
    print(lst[go[idx]], end = ' ')

n = int(input())
lst = list(map(int, input().split()))
dp = [1]*n
go = [-1]*n
Max, Maxidx = -999, 0
for i in range(n):
    st = 0
    idx = -1
    for j in range(i):
        if lst[i] > lst[j]:
           if st < dp[j]:
               st = dp[j]
               idx = j
    dp[i] = st+1
    go[i] = idx
    if Max < dp[i]:
        Max = dp[i]
        Maxidx = i

print(Max)
p(Maxidx)
print(lst[Maxidx])