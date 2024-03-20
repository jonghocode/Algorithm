# 1043(거짓말)

def find(idx):
    if idx == root[idx]:
        return root[idx]
    root[idx] = find(root[idx])
    return root[idx]

n, m = map(int, input().split())
lie = list(map(int, input().split()))
lie = lie[1:]
party = [list(map(int, input().split())) for _ in range(m)]

root = [i for i in range(n+1)]
for i in range(len(lie)-1):
    n1, n2 = find(lie[i]), find(lie[i+1])
    if n1 != n2:
        root[n2] = n1

for temp in party:
    temp = temp[1:]
    for i in range(len(temp)-1):
        n1, n2 = find(temp[i]), find(temp[i+1])
        if n1 != n2:
            root[n2] = n1
k = -1
if len(lie) >= 1:
    k = lie[0]

answer = 0
if k == -1:
    print(m)
else:
    for temp in party:
        temp = temp[1:]
        sw = 0
        for i in range(len(temp)):
            if find(k) == find(temp[i]):
                sw = 1
                break
        if sw == 0:
            answer += 1
    
    print(answer)