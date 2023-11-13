x, k = map(int, input().split())
lst = list(map(int, input().split()))
ldict, rdict = {}, {}

for i in range(2*x):
    if i < x:
        if lst[i] not in ldict:
            ldict[lst[i]] = 1
        else:
            ldict[lst[i]] += 1
    else:
        if lst[i] not in rdict:
            rdict[lst[i]] = 1
        else:
            rdict[lst[i]] += 1
answer = 0
for i in range(k+1):
    if i in ldict:
        if i in rdict:
            answer += ldict[i] * (x-rdict[i])
        else:
            answer += ldict[i] * x
print(answer)