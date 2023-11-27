find = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
adict = {}
bdict = {}

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += a[j]
        if sum not in adict:
            adict[sum] = 1
        else:
            adict[sum] += 1

for i in range(m):
    sum = 0
    for j in range(i, m):
        sum += b[j]
        if sum not in bdict:
            bdict[sum] = 1
        else:
            bdict[sum] += 1

answer = 0
for k, v in adict.items():
    if find-k in bdict:
        answer += bdict[find-k] * v

print(answer)